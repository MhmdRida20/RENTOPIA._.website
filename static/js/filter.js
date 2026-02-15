function filterOption() {
    let filter = document.getElementById("filterOption");
    let selectedFilter = filter.value;
    console.log(selectedFilter);
   /*  return selectedFilter; */
   return "Lands";
  }
  filterOption();

  if (filterOption()=="Lands") {
    disableElement();
  }
  function disableElement() {
    var elementToDisable = document.getElementById("nbRoom");
    elementToDisable.disabled=true;
    elementToDisable.remove();
}