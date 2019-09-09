// $('.card').hover(
    //   function(){ $(this).addClass('inverse') },
    //   function(){ $(this).removeClass('inverse') }
    // );


// custom select js

var x, i, j, selElmnt, a, b, c;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
for (i = 0; i < x.length; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  /* For each element, create a new DIV that will act as the selected item: */
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /* For each element, create a new DIV that will contain the option list: */
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < selElmnt.length; j++) {
    /* For each option in the original select element,
    create a new DIV that will act as an option item: */
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
        /* When an item is clicked, update the original select box,
        and the selected item: */
        var y, i, k, s, h;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        h = this.parentNode.previousSibling;
        for (i = 0; i < s.length; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            for (k = 0; k < y.length; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
          }
        }
        h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    /* When the select box is clicked, close any other select boxes,
    and open/close the current select box: */
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  /* A function that will close all select boxes in the document,
  except the current select box: */
  var x, y, i, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  for (i = 0; i < y.length; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < x.length; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);

$(document).ready(function(){
    
    
     var back = ["#90CCF4", "#f78888", "#f3d250"]
    //  var rand = back[Math.floor(Math.random()*back.length)];
     
    $('.card').hover(
       
       function(){
           var rand = back[Math.floor(Math.random()*back.length)];
           $(this).css('background-color', rand) },
       function(){ $(this).css('background-color', '#fff') }
    );
    
    $('.step').click(
        function(){ $(this).toggleClass("strikeMe")},
        );
    $('.ingredient').click(
        function(){ $(this).toggleClass("strikeMe")},
        );
    
    // document.addEventListener("DOMContentLoaded", function () {
    // setTimeout(function () {
    //     hideLoadingAni();
    //     $('.hideMe').removeClass('hideMe');
    // }, 3000);
    // return;
    // });
    
    // function loadingAni() {
    // $(".loader-wrapper").css("display", "block");
    // return;
    // }
    
    //  function hideLoadingAni() {
    // $(".loader-wrapper").css("display", "none");
    // return;
    // }
    
    // $(window).on("load",function(){
    //      $(".loader-wrapper").fadeOut("slow");
    // });
    // navbar
      
    //   overlay only displayed when sidebar selected
       $(".openbtn").click(function(){
        $(".overlay").css("display", "block")
        $(".sidebar").css("transform", "translateX(0%)")
        // Push content over
        $("body").css('overflow', 'hidden')
        
        // $(".content, .navbar, .footer").removeClass("untranslateMe")
        // $(".content, .navbar, .footer").addClass("translateMe")
        
        // $(".content, .navbar, .footer").css("transform", "translateX(250px)")
        
      });

      $(".closebtn").click(function(){
        $(".overlay").css("display", "none")
        $(".sidebar").css("transform", "translateX(-100%)")
        // Push content back
         $("body").css('overflow', 'visible')
        //  $(".content, .navbar, .footer").addClass("untranslateMe")
        //  $(".content, .navbar, .footer").removeClass("translateMe")
         
        // $(".content, .navbar, .footer").css("transform", "translateX(0px)")
      });
      
      $(".overlay").click(function(){
          $(".overlay").css("display", "none")
        $(".sidebar").css("transform", "translateX(-100%)")
        // Push content back
        //  $('body').removeClass('.overflowHidden')
        $("body").css('overflow', 'visible')
         $(".content, .navbar, .footer").addClass("untranslateMe")
         $(".content, .navbar, .footer").removeClass("translateMe")
        // $(".content", ".navbar", ".footer").css("transform", "translateX(-250px)")
      });

    
    
    var maxField = 15; //Input fields increment limitation
    var addButton = $('.add_button'); //Add button selector
    var wrapper = $('.field_wrapper'); //Input field wrapper
    var x = 1; //Initial field counter is 1
    var maxField2 = 15; //Input fields increment limitation
    var addButton2 = $('.add_button2'); //Add button selector
    var wrapper2 = $('.field_wrapper2'); //Input field wrapper
    var y = 1; //Initial field counter is 1

    //Once add button is clicked
    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append('<div><textarea class="form-control" name="recipe_ingredient" rows="1" value="" placeholder="Ingredient no. ' + x + '"></textarea><a href="#" class="remove_button">&#10008;</a></div>'); //Add field html
          
        }
    });
    
    //Once remove button is clicked
    $(wrapper).on('click', '.remove_button', function(e){
        e.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });

    //Once add button is clicked
    $(addButton2).click(function(){
        //Check maximum number of input fields
        if(y < maxField2){ 
            y++; //Increment field counter
            $(wrapper2).append('<div><textarea class="form-control" name="recipe_step" rows="2" value="" placeholder="Step no. ' + y + '"/><a href="#" class="remove_button2">&#10008;</a></div>'); //Add field html
        }
    });
    
    //Once remove button is clicked
    $(wrapper2).on('click', '.remove_button2', function(e){
        e.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });
 
});