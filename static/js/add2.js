function openAddElementPage() {
  var form = document.createElement("form");
  form.className = "added_form";
  form.action = "/insert_land";
  form.method = "POST";
form.enctype="multipart/form-data";
  var innerHTML = `
    <div class="add_image1">
    <input type="file" name="in" placeholder="images" id="in">
    <input type="file" name="in2" placeholder="images" id="in2">
    <input type="file" name="in3" placeholder="images" id="in3">
    <input type="file" name="in4" placeholder="images" id="in4">
    </div>
    <div>
      <div class="info">
        <input type="text" placeholder="Price for one day" name="price" id="priceInput">
        <input type="text" placeholder="Area" name="area" id="areaInput">
        
      
        <input type="text" placeholder="location_link" name="location_link" id="location_linkInput">
      </div>
      <div class="info">
        
        <select class="select" placeholder="Location" name="location" id="locationInput">
          <option disabled selected>Location</option>
          <option value="South Of Lebanon">South Of Lebanon</option>
          <option value="North Of Lebanon">North Of Lebanon</option>
          <option value="East Of Lebanon">East Of Lebanon</option>
          <option value="Center Of Lebanon">Center Of Lebanon</option>
          <option value="ALL">ALL</option>
        </select>
      </div>
    </div>
    <button id="confirmButton" type="submit" >Confirm</button>
    
  `;

  form.innerHTML = innerHTML;
  document.getElementById("add").innerHTML = "";
  document.getElementById("add").appendChild(form);
}

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("newi").addEventListener("click", openAddElementPage);
});



