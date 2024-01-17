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
                H_Value: $("#H_out").text(),
                S_Value: $("#S_out").text(),
                V_Value: $("#V_out").text(),
                Thresh_value: $("#Thresh_out").text(),
                
            },
        });
    });
});

function ShowImage() {
    var checkBox_color = document.getElementById("check-color");
    var color = document.getElementById("img-color");

    var checkBox_hsv = document.getElementById("check-hsv");
    var hsv = document.getElementById("img-hsv");

    var checkBox_pallet = document.getElementById("check-pallet");
    var pallet = document.getElementById("img-pallet");

    var checkBox_process = document.getElementById("check-process");
    var process = document.getElementById("img-process");
    
    if (checkBox_color.checked == true){
        color.style.display = "flex";
    } else {
        color.style.display = "none";
    }
    if (checkBox_hsv.checked == true){
        hsv.style.display = "flex";
    } else {
        hsv.style.display = "none";
    }
    if (checkBox_pallet.checked == true){
        pallet.style.display = "flex";
    } else {
        pallet.style.display = "none";
    }
    if (checkBox_process.checked == true){
        process.style.display = "flex";
    } else {
        process.style.display = "none";
    }
  }
var H_in = document.getElementById("H_in");
var H_out = document.getElementById("H_out");
var S_in = document.getElementById("S_in");
var S_out = document.getElementById("S_out");
var V_in = document.getElementById("V_in");
var V_out = document.getElementById("V_out");
var Thresh_in = document.getElementById("Thresh_in");
var Thresh_out = document.getElementById("Thresh_out");
H_out.innerHTML1 = H_in.value1;
S_out.innerHTML2 = S_in.value2;
V_out.innerHTML3 = V_in.value3;
Thresh_out.innerHTML4 = Thresh_in.value4;

H_in.oninput = function() {
    H_out.innerHTML = this.value;
}
S_in.oninput = function() {
    S_out.innerHTML = this.value;
}
V_in.oninput = function() {
    V_out.innerHTML = this.value;
}
Thresh_in.oninput = function() {
    Thresh_out.innerHTML = this.value;
}
