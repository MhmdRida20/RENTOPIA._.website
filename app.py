from flask import Flask, jsonify, request, redirect, url_for, render_template,session,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_
from flask import jsonify
from sqlalchemy import text
import os
from urllib.parse import urlencode
from PIL import Image
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Mhmdali$@localhost/rentopia'
app.config['SECRET_KEY'] = 'your_secret_key'


db = SQLAlchemy(app)
login_manager = LoginManager(app) 

with app.app_context():
    db.Model.metadata.reflect(db.engine)

# Define User Model
class User(UserMixin, db.Model):
    __table__ = db.metadata.tables['users']
    def get_id(self):
        return str(self.user_id)
class Card(UserMixin, db.Model):
    __table__ = db.metadata.tables['cards']
    
class Lands(UserMixin,db.Model):
    __table__ = db.metadata.tables['lands']
class Shops(UserMixin,db.Model):
    __table__ = db.metadata.tables['shops']
class Apartments(UserMixin,db.Model):
    __table__ = db.metadata.tables['apartments']

class Feedbacks(UserMixin,db.Model):
    __table__=db.metadata.tables['feedbacks']
# User Loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))   

@app.route('/signup2')
def signup2():
    return render_template("sign_up.html")
@app.route('/login2')
def login2():
    return render_template("log_in.html")
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return render_template("index.html")
    if request.method == 'POST':
        email = request.form['email']
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        birthdate = request.form.get("date_birth")
        file=request.files['profilephoto']
        if not email or not fullname or not username or not password or not phone or not birthdate or not file:
            return redirect(url_for('signup2'))
        if file.filename:
            file_path = os.path.join(app.root_path, 'static/img', file.filename)
            file.save(file_path)
            profilephoto = os.path.join('static/img', file.filename)
        else:
            # Use a default image path if no file is provided
            default_image = 'static/img/profile_icon.png'
            profilephoto = default_image

        new_user = User(email=email, full_name=fullname, username=username, password=generate_password_hash(password), phone=phone, birthdate=birthdate, role="user", profilephoto=profilephoto)        
        if username=="admin":
            new_user.role="admin"
        db.session.add(new_user)
        db.session.commit()
        
        # Log in the newly registered user
        login_user(new_user)
        
        return redirect(url_for('home'))
        
    return render_template('sign_up.html')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login1():
    if current_user.is_authenticated:
        return render_template('index.html')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if not email or not password:
            return redirect(url_for('login2'))
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template('index.html', error='Invalid email or password. Please try again.')
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()  # Clear session data
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


@app.route("/addElement2")
def addElement2():
    return render_template("addElement.html")

@app.route("/birth_profile2")
def birth_profile2():
    return render_template("birth_profile.html")




@app.route("/feedbacks2")
def feedbacks2():
    feedbacks=db.session.execute(text('SELECT * FROM feedbacks')).fetchall()
    return render_template("feedbacks.html",feedbacks=feedbacks)


@app.route('/filter2')
def filter2():
    return render_template('filter.html')


@app.route("/learnmore2")
def learnmore2():
    return render_template("learnmore.html")


@app.route("/payment2/<int:land_id>")
def payment2(land_id):
    return render_template("payment.html", land_id=land_id)

@app.route("/api/payment/<int:land_id>", methods=["POST"])
def payment(land_id):
    name_card = request.form.get('name_card')
    card_number = int(request.form.get('cardNumber'))
    cvv = int(request.form.get('cvv'))
    card = Card.query.filter_by(cardNumber=card_number, nameCard=name_card, cvv=cvv).first()
    land = Lands.query.get_or_404(land_id)
    price = land.price
    rent_until_date = request.form.get('rent_until')

    today_date = datetime.today().date()

    chosen_date = datetime.strptime(rent_until_date, '%Y-%m-%d').date()

    difference = chosen_date - today_date

    number_of_days = difference.days

    total_price = price * number_of_days 

    if card is not None and card.balance >= total_price:
        card.balance -= total_price
        land.status = "rent"
        land.datee = rent_until_date
        db.session.commit()
        return jsonify({"success": True, "message": "Payment completed successfully!"})
    else:
        return jsonify({"success": False, "error": "This card is not available or does not have sufficient balance!"}), 403
    
 
@app.route("/payment4/<int:shop_id>")
def payment4(shop_id):
    return render_template("payment3.html", shop_id=shop_id)


@app.route("/api/payment3/<int:shop_id>", methods=["POST"])
def payment3(shop_id):
    name_card = request.form.get('name_card')
    card_number = int(request.form.get('cardNumber'))
    cvv = int(request.form.get('cvv'))
    card = Card.query.filter_by(cardNumber=card_number, nameCard=name_card, cvv=cvv).first()
    shop = Shops.query.get_or_404(shop_id)
    price = shop.price
    rent_until_date = request.form.get('rent_until')

    today_date = datetime.today().date()

    chosen_date = datetime.strptime(rent_until_date, '%Y-%m-%d').date()

    difference = chosen_date - today_date

    number_of_days = difference.days

    total_price = price * number_of_days

 

    if card is not None and card.balance >= total_price:
        card.balance -= total_price
        shop.status = "rent"
        shop.datee = rent_until_date
        db.session.commit()
        return jsonify({"success": True, "message": "Payment completed successfully!"})
    else:
        return jsonify({"success": False, "error": "This card is not available or does not have sufficient balance!"}), 403
    

@app.route("/payment6/<int:apartment_id>")
def payment6(apartment_id):
    return render_template("payment5.html", apartment_id=apartment_id)


@app.route("/api/payment5/<int:apartment_id>", methods=["POST"])
def payment5(apartment_id):
    name_card = request.form.get('name_card')
    card_number = int(request.form.get('cardNumber'))
    cvv = int(request.form.get('cvv'))
    card = Card.query.filter_by(cardNumber=card_number, nameCard=name_card, cvv=cvv).first()
    apartment= Apartments.query.get_or_404(apartment_id)
    price = apartment.price
    rent_until_date = request.form.get('rent_until')

    today_date = datetime.today().date()

    chosen_date = datetime.strptime(rent_until_date, '%Y-%m-%d').date()

    difference = chosen_date - today_date

    number_of_days = difference.days

    total_price = price * number_of_days


    if card is not None and card.balance >= total_price:
        card.balance -= total_price
        apartment.status = "rent"
        apartment.datee = rent_until_date
        db.session.commit()
        return jsonify({"success": True, "message": "Payment completed successfully!"})
    else:
        return jsonify({"success": False, "error": "This card is not available or does not have sufficient balance!"}), 403
    
@app.route('/home', methods=['GET'])
def home():
    lands = db.session.execute(text('SELECT * FROM lands')).fetchall()
    apartments = db.session.execute(text('SELECT * FROM apartments')).fetchall()
    shops = db.session.execute(text('SELECT * FROM shops')).fetchall()
    feedbacks = db.session.execute(text('SELECT * FROM feedbacks LIMIT 5')).fetchall()
    return render_template('home.html', lands=lands, apartments=apartments, shops=shops, feedbacks=feedbacks)

@app.route('/lands')
def lands():
    update_land_status()
    lands = Lands.query.all()
    return render_template('lands.html', lands=lands)
def update_land_status():
    today = datetime.today().date()
    lands_to_update = Lands.query.filter(Lands.datee <= today, Lands.status == 'rent').all()
    for land in lands_to_update:
        land.status = 'available'
    db.session.commit() 

@app.route('/shops')
def shops():
    update_shop_status()
    shops = db.session.execute(text('SELECT * FROM shops')).fetchall()
    
    return render_template('shops.html', shops=shops)


@app.route('/apartments')
def apartments():
    update_apartment_status()
    apartments = db.session.execute(text('SELECT * FROM apartments')).fetchall()
    
    return render_template('appartment.html', apartments=apartments)




@app.route('/insert_land', methods=['POST'])
def insert_land():
   
        price = request.form['price']
        area = request.form['area']
        location = request.form.get('location', '')
        location_link=request.form['location_link']
        file = request.files['in']
        file2 = request.files['in2']
        file3 = request.files['in3']
        file4= request.files['in4']
        phone=current_user.phone
        
        if not price or not area or location=="" or not file or not file2 or not file3 or not file4 or not location_link or not phone :
        
            return redirect(url_for('lands'))
        file_path = os.path.join(app.root_path, 'static\\img', file.filename)
        file.save(file_path)
        
        file_path2 = os.path.join(app.root_path, 'static\\img', file2.filename)
        file2.save(file_path2)
        
        file_path3 = os.path.join(app.root_path, 'static\\img', file3.filename)
        file3.save(file_path3)
        
        file_path4 = os.path.join(app.root_path, 'static\\img', file4.filename)
        file4.save(file_path4)
        newland = Lands(price=price, area=area, location=location,image= os.path.join('/static/img/', file.filename),image2= os.path.join('/static/img/', file2.filename),image3= os.path.join('/static/img/', file3.filename),image4= os.path.join('/static/img/', file4.filename),location_link=location_link ,phone=phone)
        db.session.add(newland)
        
        db.session.commit()
        """ update_land_status() """
        return redirect(url_for('lands'))





@app.route('/api/delete_land/<int:land_id>', methods=['DELETE'])
def delete_land(land_id):
    if current_user.role == 'admin':
        land = Lands.query.get_or_404(land_id)
        db.session.delete(land)
        db.session.commit()
        return jsonify({'message': 'Land deleted successfully'})
    else:
        return jsonify({'error': 'You are a user and cannot delete lands.'}), 403

@app.route('/details/<int:land_id>')
def details(land_id):
    land = Lands.query.get(land_id)
    
    return render_template('details.html', land=land)





def update_shop_status():
    today = datetime.today().date()
    shops_to_update = Shops.query.filter(Shops.datee <= today, Shops.status == 'rent').all()
    for shop in shops_to_update:
        shop.status = 'available'
    db.session.commit()


@app.route('/insert_shop', methods=['POST'])
def insert_shop():
   
        price = request.form['price']
        area = request.form['area']
        location = request.form.get('location', '')
        bathroom=request.form['bathroom']
        location_link=request.form['location_link']
        file = request.files['in']
        file2 = request.files['in2']
        file3 = request.files['in3']
        file4= request.files['in4']
        phone=current_user.phone
        
        if not price or not area or location=="" or not bathroom or not file or not file2 or not file3 or not file4 or not location_link or not phone :
        
            return redirect(url_for('shops'))
        file_path = os.path.join(app.root_path, 'static\\img', file.filename)
        file.save(file_path)
        
        file_path2 = os.path.join(app.root_path, 'static\\img', file2.filename)
        file2.save(file_path2)
        
        file_path3 = os.path.join(app.root_path, 'static\\img', file3.filename)
        file3.save(file_path3)
        
        file_path4 = os.path.join(app.root_path, 'static\\img', file4.filename)
        file4.save(file_path4)
        newshop = Shops(price=price, area=area, location=location,bathroom=bathroom,image= os.path.join('/static/img/', file.filename),image2= os.path.join('/static/img/', file2.filename),image3= os.path.join('/static/img/', file3.filename),image4= os.path.join('/static/img/', file4.filename),location_link=location_link,phone=phone)
        db.session.add(newshop)
        
        db.session.commit()
        
        return redirect(url_for('shops'))





@app.route('/api/delete_shop/<int:shop_id>', methods=['DELETE'])
def delete_shop(shop_id):
    if current_user.role == 'admin':
        shop = Shops.query.get_or_404(shop_id)
        db.session.delete(shop)
        db.session.commit()
        return jsonify({'message': 'Shop deleted successfully'})
    else:
        return jsonify({'error': 'You are a user and cannot delete shops.'}), 403

@app.route('/details2/<int:shop_id>')
@login_required
def details2(shop_id):
    shop = Shops.query.get(shop_id)
    return render_template('details2.html', shop=shop)


def update_apartment_status():
    today = datetime.today().date()
    apartments_to_update = Apartments.query.filter(Apartments.datee <= today, Apartments.status == 'rent').all()
    for apartment in apartments_to_update:
        apartment.status = 'available'
    db.session.commit()



@app.route('/insert_apartment', methods=['POST'])
def insert_apartment(): 
        price = request.form['price']
        area = request.form['area']
        location = request.form.get('location', '')
        bathroom=request.form['bathroom']
        bedroom = request.form['bedroom']
        floor=request.form['floor']
        location_link=request.form['location_link']
        file = request.files['in']
        file2 = request.files['in2']
        file3 = request.files['in3']
        file4= request.files['in4']
        phone=current_user.phone
        
        if not price or not area or location=="" or not bathroom or not bedroom or not floor or not file or not file2 or not file3 or not file4 or not location_link or not phone :
        
            return redirect(url_for('apartments'))
        file_path = os.path.join(app.root_path, 'static\\img', file.filename)
        file.save(file_path)
        
        file_path2 = os.path.join(app.root_path, 'static\\img', file2.filename)
        file2.save(file_path2)
        
        file_path3 = os.path.join(app.root_path, 'static\\img', file3.filename)
        file3.save(file_path3)
        
        file_path4 = os.path.join(app.root_path, 'static\\img', file4.filename)
        file4.save(file_path4)
        newapartment = Apartments(price=price, area=area, location=location,bathroom=bathroom,bedroom=bedroom,floor=floor,image= os.path.join('/static/img/', file.filename),image2= os.path.join('/static/img/', file2.filename),image3= os.path.join('/static/img/', file3.filename),image4= os.path.join('/static/img/', file4.filename),location_link=location_link ,phone=phone)
        db.session.add(newapartment)
        
        db.session.commit()
        
        return redirect(url_for('apartments'))

@app.route('/api/delete_apartment/<int:apartment_id>', methods=['DELETE'])
def delete_apartment(apartment_id):
    if current_user.role == 'admin':
        apartment = Apartments.query.get_or_404(apartment_id)
        db.session.delete(apartment)
        db.session.commit()
        return jsonify({'message': 'apartment deleted successfully'})
    else:
        return jsonify({'error': 'You are a user and cannot delete apartment.'}), 403

@app.route('/details3/<int:apartment_id>')
def details3(apartment_id):
    apartment = Apartments.query.get(apartment_id)
    return render_template('details3.html', apartment=apartment)


@app.route('/insert_feedback' ,methods=['POST'])
def insert_feedback():
    username=current_user.username
    feedback=request.form['feedback']
    profilephoto=current_user.profilephoto
    newfeedback=Feedbacks(feedback=feedback,username=username,profilephoto=profilephoto)
    if not feedback :
        return redirect(url_for("feedbacks2"))
    db.session.add(newfeedback)
    db.session.commit()
    return redirect(url_for("feedbacks2"))

@app.route('/filter3', methods=['POST'])
def filter3():
    filter_name= request.form.get('filter_name_test')
    price = request.form.get('price')
    area = request.form.get('area')
    location = request.form.get('location')
    query = "SELECT * FROM "+filter_name+" WHERE 1=1 "
    if price=="price1":
        query += " AND price>= 1 and price <=30"
    if price=="price2":
        query += " AND price>= 30 and price <=90"
    if price=="price3":
        query += " AND price>90"
    if area != 'ALL':
        if area=="area1":
            query += " AND area>= 70 and area <=150 "
        if area=="area2":
            query += " AND area>= 150 and area <=250 "
        if area=="area3":
            query += " AND area>= 250 and area <=1000 "
        if area=="area4":
            query += " AND area>=1000"
    if location !='ALL':
        if location=="location1":
            query += " AND location = 'South Of Lebanon'"
        if location=="location2":
            query += " AND location = 'North Of Lebanon'"
        if location=="location3":
            query += " AND location = 'East Of Lebanon'"
        if location=="location4":
            query += " AND location = 'Center Of Lebanon'"
    appartment_test=db.session.execute(text(query + " order by price asc")).fetchall()
    
    if filter_name=="apartments":
        return render_template('appartment.html', apartments=appartment_test)
    if filter_name=="shops":
        return render_template('shops.html', shops=appartment_test)
    if filter_name=="lands":
        return render_template('lands.html', lands=appartment_test)

    return render_template('apartments.html', apartments=appartment_test)
    

if __name__ == '__main__':
    app.run(debug=True) 



