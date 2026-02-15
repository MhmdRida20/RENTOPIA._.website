window.addEventListener('DOMContentLoaded', (event) => {
  const params = new URLSearchParams(window.location.search);
  const itemType = params.get('type');
  if (itemType === 'shop') {
    const bedroomElement = document.getElementById("bedroom");
    bedroomElement.innerHTML += "  NONE";
    bedroomElement.style.color = "red";
    const floorElement = document.getElementById("floor");
    floorElement.innerHTML += "   NONE";
    floorElement.style.color = "red"; 
  } else if (itemType === 'land') {
    const bathroomElement = document.getElementById("bathroom");
    bathroomElement.innerHTML += "   NONE";
    bathroomElement.style.color = "red"; 
    const bedroomElement = document.getElementById("bedroom");
    bedroomElement.innerHTML += "   NONE";
    bedroomElement.style.color = "red";
    const floorElement = document.getElementById("floor");
    floorElement.innerHTML += "   NONE";
    floorElement.style.color = "red"; 
  }
});
