$(document).ready(function(){

    $('#selection-toggle').click(function(){
        $("#selecting").toggle();
    });
    $('#slider-toggle').click(function(){
        $("#slider").toggle();
    });
    $(".button-upadte").click(function(){
        $.ajax({
            data:{
                thresh_A_Value: $("#Thresh_a_out").text(),
                thresh_B_Value: $("#thresh_b_out").text(),
                
            },
        });
    });
    
    
});

function ShowImage() {
    var checkBox_color = document.getElementById("check-color");
    var color = document.getElementById("img-color");

    var checkBox_Line = document.getElementById("check-Line");
    var Line = document.getElementById("img-line");

    var checkBox_Line_process = document.getElementById("check-Line-process");
    var Line_process = document.getElementById("img-line-process");
    
    if (checkBox_color.checked == true){
        color.style.display = "flex";
    } else {
        color.style.display = "none";
    }
    if (checkBox_Line.checked == true){
        Line.style.display = "flex";
    } else {
        Line.style.display = "none";
    }

    if (checkBox_Line_process.checked == true){
        Line_process.style.display = "flex";
    } else {
        Line_process.style.display = "none";
    }
    
    
  }
  var thresh_a_in = document.getElementById("thresh_a_in");
  var Thresh_a_out = document.getElementById("Thresh_a_out");
  var thresh_b_in = document.getElementById("thresh_b_in");
  var thresh_b_out = document.getElementById("thresh_b_out");


  Thresh_a_out.innerHTML1 = thresh_a_in.value1;
  thresh_b_out.innerHTML2 = thresh_b_in.value2;


  
  thresh_a_in.oninput = function() {
    Thresh_a_out.innerHTML = this.value;
  }
  thresh_b_in.oninput = function() {
    thresh_b_out.innerHTML = this.value;
  }

