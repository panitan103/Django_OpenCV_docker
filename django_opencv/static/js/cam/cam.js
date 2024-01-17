function ShowImage() {
    var checkBox_color = document.getElementById("check-color");
    var color = document.getElementById("img-color");

    var checkBox_gray = document.getElementById("check-gray");
    var gray = document.getElementById("img-gray");
    
    if (checkBox_color.checked == true){
        color.style.display = "flex";
    } else {
        color.style.display = "none";
    }
    if (checkBox_gray.checked == true){
        gray.style.display = "flex";
    } else {
        gray.style.display = "none";
    }
}
$(document).ready(function(){

    $('#selection-toggle').click(function(){
        $("#selecting").toggle();
    });
    
  
});