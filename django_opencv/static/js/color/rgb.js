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
                R_Value: $("#R_out").text(),
                G_Value: $("#G_out").text(),
                B_Value: $("#B_out").text(),
                Thresh_value: $("#Thresh_out").text(),
                
            },
        });
    });
});

function ShowImage() {
    var checkBox_color = document.getElementById("check-color");
    var color = document.getElementById("img-color");

    var checkBox_rgb = document.getElementById("check-rgb");
    var rgb = document.getElementById("img-rgb");

    var checkBox_pallet = document.getElementById("check-pallet");
    var pallet = document.getElementById("img-pallet");

    var checkBox_Process = document.getElementById("check-Process");
    var process = document.getElementById("img-process");
    
    if (checkBox_color.checked == true){
        color.style.display = "flex";
    } else {
        color.style.display = "none";
    }

    if (checkBox_rgb.checked == true){
        rgb.style.display = "flex";
    } else {
        rgb.style.display = "none";
    }

    if (checkBox_pallet.checked == true){
        pallet.style.display = "flex";
    } else {
        pallet.style.display = "none";
    }

    if (checkBox_Process.checked == true){
        process.style.display = "flex";
    } else {
        process.style.display = "none";
    }
  }
  var R_in = document.getElementById("R_in");
  var R_out = document.getElementById("R_out");
  var G_in = document.getElementById("G_in");
  var G_out = document.getElementById("G_out");
  var B_in = document.getElementById("B_in");
  var B_out = document.getElementById("B_out");
  var Thresh_in = document.getElementById("Thresh_in");
  var Thresh_out = document.getElementById("Thresh_out");
  R_out.innerHTML1 = R_in.value1;
  G_out.innerHTML2 = G_in.value2;
  B_out.innerHTML3 = B_in.value3;
  Thresh_out.innerHTML4 = Thresh_in.value4;
  
  R_in.oninput = function() {
      R_out.innerHTML = this.value;
  }
  G_in.oninput = function() {
      G_out.innerHTML = this.value;
  }
  B_in.oninput = function() {
      B_out.innerHTML = this.value;
  }
  Thresh_in.oninput = function() {
      Thresh_out.innerHTML = this.value;
  }