$(document).ready(function(){

    $('#selection-toggle').click(function(){
        $("#selecting").toggle();
    });
    $('#slider-toggle').click(function(){
        $("#slider").toggle();
    });
    $(".button-thresh").click(function(){
        $.ajax({
            data:{
                thresh_morp_Value: $("#Thresh_morp_out").text(),
                kern_Value: $("#kern_out").text(),
                iter_Value: $("#iter_out").text(),
                thresh_morp_type: parseInt("0"),
            },
        });
    });
    $(".button-thresh-inv").click(function(){
        $.ajax({
            data:{
                thresh_morp_Value: $("#Thresh_morp_out").text(),
                kern_Value: $("#kern_out").text(),
                iter_Value: $("#iter_out").text(),
                thresh_morp_type: parseInt("1"),
            },
        });
    });
    
    
});

function ShowImage() {
    var checkBox_color = document.getElementById("check-color");
    var color = document.getElementById("img-color");

    var checkBox_contour = document.getElementById("check-contour");
    var contour = document.getElementById("img-contour");

    var checkBox_morph = document.getElementById("check-morph");
    var morph = document.getElementById("img-morph");
    
    if (checkBox_color.checked == true){
        color.style.display = "flex";
    } else {
        color.style.display = "none";
    }
    if (checkBox_contour.checked == true){
        contour.style.display = "flex";
    } else {
        contour.style.display = "none";
    }
    if (checkBox_morph.checked == true){
        morph.style.display = "flex";
    } else {
        morph.style.display = "none";
    }
  }
  var Thresh_morp_in = document.getElementById("Thresh_morp_in");
  var Thresh_morp_out = document.getElementById("Thresh_morp_out");
  var kern_in = document.getElementById("kern_in");
  var kern_out = document.getElementById("kern_out");
  var iter_in = document.getElementById("iter_in");
  var iter_out = document.getElementById("iter_out");

  Thresh_morp_out.innerHTML1 = Thresh_morp_in.value1;
  kern_out.innerHTML2 = kern_in.value2;
  iter_out.innerHTML3 = iter_in.value3;

  
  Thresh_morp_in.oninput = function() {
    Thresh_morp_out.innerHTML = this.value;
  }
  kern_in.oninput = function() {
    kern_out.innerHTML = this.value;
  }
  iter_in.oninput = function() {
    iter_out.innerHTML = this.value;
  }
