# Rentopia 🏠

A modern rental property management web application built with Flask. Rentopia allows users to browse, list, and rent various types of properties including lands, shops, and apartments.

## Features

### For Users
- **User Authentication**: Secure registration and login system with profile photos
- **Property Listings**: Browse available lands, shops, and apartments
- **Property Details**: View detailed information about each property with multiple images
- **Property Filtering**: Filter properties by price, area, and location (North, South, East, Center of Lebanon)
- **Rental System**: Rent properties for specified periods with automatic status updates
- **Payment Processing**: Secure card-based payment system for rentals
- **User Feedback**: Leave and view feedback from other users
- **Profile Management**: Personalized profiles with profile photos

### For Admins
- **Property Management**: Delete any property from the platform
- **User Roles**: Admin and regular user roles

## Tech Stack

- **Backend**: Python, Flask
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap 5
- **Image Processing**: Pillow (PIL)

## Project Structure

```
rentopia_git/
├── app.py                  # Main Flask application
├── static/
│   ├── css/               # Stylesheets
│   │   ├── addElement.css
│   │   ├── appartment.css
│   │   ├── birth_profile.css
│   │   ├── category.css
│   │   ├── details.css
│   │   ├── feedbacks.css
│   │   ├── filter.css
│   │   ├── home.css
│   │   ├── index.css
│   │   ├── learnmore.css
│   │   ├── log_in.css
│   │   ├── payment.css
│   │   └── sign_up.css
│   ├── js/                # JavaScript files
│   │   ├── add2.js
│   │   ├── add3.js
│   │   ├── add4.js
│   │   ├── birth_profile.js
│   │   ├── details.js
│   │   ├── filter.js
│   │   ├── login.js
│   │   ├── payment.js
│   │   ├── payment3.js
│   │   ├── payment5.js
│   │   └── signup.js
│   └── img/               # Images and assets
└── templates/             # HTML templates
    ├── addElement.html
    ├── appartment.html
    ├── birth_profile.html
    ├── details.html
    ├── details2.html
    ├── details3.html
    ├── feedbacks.html
    ├── filter.html
    ├── home.html
    ├── index.html
    ├── lands.html
    ├── learnmore.html
    ├── log_in.html
    ├── payment.html
    ├── payment3.html
    ├── payment5.html
    ├── shops.html
    └── sign_up.html
```

## Database Schema

The application uses the following database tables:

| Table | Description |
|-------|-------------|
| `users` | User accounts with profile information |
| `cards` | Payment cards for rental transactions |
| `lands` | Land property listings |
| `shops` | Shop/retail space listings |
| `apartments` | Apartment listings |
| `feedbacks` | User feedback and reviews |

## Installation

### Prerequisites

- Python 3.8 or higher
- MySQL Server
- pip (Python package manager)

### Step 1: Clone the Repository

```
bash
git clone <repository-url>
cd rentopia_git
```

### Step 2: Create Virtual Environment

```
bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows:**
```
bash
venv\Scripts\activate
```

**Mac/Linux:**
```
bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```
bash
pip install flask flask-sqlalchemy flask-login werkzeug pillow
```

### Step 5: Configure Database

1. Open MySQL and create a database named `rentopia`:

```
sql
CREATE DATABASE rentopia;
```

2. Update the database connection string in `app.py` if needed:

```
python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:your_password@localhost/rentopia'
```

3. Create the required tables. The application uses SQLAlchemy's reflection feature, so tables must exist in the database. Run the following SQL to create the necessary tables:

```
sql
-- Users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    birthdate DATE,
    role VARCHAR(20) DEFAULT 'user',
    profilephoto VARCHAR(255)
);

-- Cards table
CREATE TABLE cards (
    card_id INT AUTO_INCREMENT PRIMARY KEY,
    nameCard VARCHAR(255) NOT NULL,
    cardNumber BIGINT UNIQUE NOT NULL,
    cvv INT NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 10000.00
);

-- Lands table
CREATE TABLE lands (
    land_id INT AUTO_INCREMENT PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    area DECIMAL(10, 2) NOT NULL,
    location VARCHAR(255),
    image VARCHAR(255),
    image2 VARCHAR(255),
    image3 VARCHAR(255),
    image4 VARCHAR(255),
    location_link VARCHAR(500),
    phone VARCHAR(20),
    status VARCHAR(20) DEFAULT 'available',
    datee DATE
);

-- Shops table
CREATE TABLE shops (
    shop_id INT AUTO_INCREMENT PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    area DECIMAL(10, 2) NOT NULL,
    location VARCHAR(255),
    bathroom INT,
    image VARCHAR(255),
    image2 VARCHAR(255),
    image3 VARCHAR(255),
    image4 VARCHAR(255),
    location_link VARCHAR(500),
    phone VARCHAR(20),
    status VARCHAR(20) DEFAULT 'available',
    datee DATE
);

-- Apartments table
CREATE TABLE apartments (
    apartment_id INT AUTO_INCREMENT PRIMARY KEY,
    price DECIMAL(10, 2) NOT NULL,
    area DECIMAL(10, 2) NOT NULL,
    location VARCHAR(255),
    bathroom INT,
    bedroom INT,
    floor INT,
    image VARCHAR(255),
    image2 VARCHAR(255),
    image3 VARCHAR(255),
    image4 VARCHAR(255),
    location_link VARCHAR(500),
    phone VARCHAR(20),
    status VARCHAR(20) DEFAULT 'available',
    datee DATE
);

-- Feedbacks table
CREATE TABLE feedbacks (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    feedback TEXT,
    profilephoto VARCHAR(255)
);
```

### Step 6: Run the Application

```
bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

## Usage Guide

### Registration & Login
1. Visit the homepage and click "Sign Up"
2. Fill in your details including email, full name, username, password, phone, birthdate, and upload a profile photo
3. Login with your credentials

### Browsing Properties
1. From the home page, view featured listings
2. Use the "Categories" dropdown to view specific property types (Apartments, Lands, Shops)
3. Click on any property to see detailed information

### Filtering Properties
1. Click the "Filter" button on the navigation bar
2. Filter by:
   - Price range (1-30, 30-90, 90+)
   - Area (70-150, 150-250, 250-1000, 1000+ sq meters)
   - Location (South/North/East/Center of Lebanon)

### Adding a Property
1. Navigate to the category you want to add (Lands, Shops, or Apartments)
2. Click on "Add Element" or similar option
3. Fill in property details and upload up to 4 images

### Renting a Property
1. View property details
2. Click "Rent" or "Payment"
3. Enter card details (name, card number, CVV)
4. Select rental period
5. Confirm payment - the property status will change to "rent"

### Leaving Feedback
1. Click on "Feedbacks" in the navigation
2. Submit your feedback

### Admin Functions
- If you register with username "admin", you will have admin privileges
- Admins can delete any property from the platform

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home/Index page |
| `/signup` | GET, POST | User registration |
| `/login` | GET, POST | User login |
| `/logout` | GET | User logout |
| `/home` | GET | Dashboard with listings |
| `/lands` | GET | Lands listing |
| `/shops` | GET | Shops listing |
| `/apartments` | GET | Apartments listing |
| `/details/<id>` | GET | Land details |
| `/details2/<id>` | GET | Shop details |
| `/details3/<id>` | GET | Apartment details |
| `/filter2` | GET | Filter page |
| `/filter3` | POST | Apply filters |
| `/payment2/<id>` | GET | Land payment page |
| `/payment4/<id>` | GET | Shop payment page |
| `/payment6/<id>` | GET | Apartment payment page |
| `/api/payment/<id>` | POST | Process land payment |
| `/api/payment3/<id>` | POST | Process shop payment |
| `/api/payment5/<id>` | POST | Process apartment payment |
| `/insert_land` | POST | Add new land |
| `/insert_shop` | POST | Add new shop |
| `/insert_apartment` | POST | Add new apartment |
| `/insert_feedback` | POST | Add feedback |
| `/api/delete_land/<id>` | DELETE | Delete land (admin) |
| `/api/delete_shop/<id>` | DELETE | Delete shop (admin) |
| `/api/delete_apartment/<id>` | DELETE | Delete apartment (admin) |

## Demo Account

For testing purposes, you can use the following demo card details:
- **Name**: Test Card
- **Card Number**: 1234567890
- **CVV**: 123
- **Balance**: $10,000

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Bootstrap 5 for the UI components
- Flask community for the excellent documentation
- All contributors who have helped improve this project

---
Author:
Mohamad Rida
