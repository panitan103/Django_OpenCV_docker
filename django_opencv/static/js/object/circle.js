$(document).ready(function(){

    $('#selection-toggle').click(function(){
        $("#selecting").toggle();
    });
    $('#slider-toggle').click(function(){
        $("#slider").toggle();
    });
    $(".button-update").click(function(){
        $.ajax({
            data:{
                param1_out: $("#param1_out").text(),
                param2_out: $("#param2_out").text(),
                minRadius_out: $("#minRadius_out").text(),
                maxRadius_out: $("#maxRadius_out").text(),
                
                
            },
        });
    });
});

function ShowImage() {
    var checkBox_color = document.getElementById("check-color");
    var color = document.getElementById("img-color");

    var checkBox_circle = document.getElementById("check-circle");
    var circle = document.getElementById("img-circle");

    
    if (checkBox_color.checked == true){
        color.style.display = "flex";
    } else {
        color.style.display = "none";
    }
    if (checkBox_circle.checked == true){
        circle.style.display = "flex";
    } else {
        circle.style.display = "none";
    }

  }
var param1_in = document.getElementById("param1_in");
var param1_out = document.getElementById("param1_out");
var param2_in = document.getElementById("param2_in");
var param2_out = document.getElementById("param2_out");
var minRadius_in = document.getElementById("minRadius_in");
var minRadius_out = document.getElementById("minRadius_out");
var maxRadius_in = document.getElementById("maxRadius_in");
var maxRadius_out = document.getElementById("maxRadius_out");

param1_out.innerHTML1 = param1_in.value1;
param2_out.innerHTML2 = param2_in.value2;
minRadius_out.innerHTML3 = minRadius_in.value3;
maxRadius_out.innerHTML3 = maxRadius_in.value3;



param1_in.oninput = function() {
    param1_out.innerHTML = this.value;
}
param2_in.oninput = function() {
    param2_out.innerHTML = this.value;
}
minRadius_in.oninput = function() {
    minRadius_out.innerHTML = this.value;
}
maxRadius_in.oninput = function() {
    maxRadius_out.innerHTML = this.value;
}
