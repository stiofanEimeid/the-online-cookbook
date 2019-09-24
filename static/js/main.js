/* global dc */
/* global $ */
/* global queue */
/* global d3 */
/* global crossfilter*/

$(document).ready(function(){
    
$('#myTooltip').tooltip();

$('#mySecondTooltip').tooltip();
    
    // Colour group
    var back = ["#90CCF4", "#f78888", "#f3d250"];
     
    $('.card').hover(
       function(){
        /* A random colour is chosen from the colour group and set as the 
         card background on hover */
           var rand = back[Math.floor(Math.random()*back.length)];
           $(this).css('background-color', rand);
       },
            function(){ $(this).css('background-color', '#fff');
       }
    );
    
    // Strike-through property toggled on click for steps and ingredients in recipe page
    $('.step').click(
        function(){ $(this).toggleClass("strikeMe");}
        );
    $('.ingredient').click(
        function(){ $(this).toggleClass("strikeMe");}
        );
      
    //   overlay only displayed when sidebar selected
       $(".openbtn" ).click(function(){
        $(".overlay").css("display", "block");
        $(".sidebar").css("transform", "translateX(0%)");
        // Prevents user from scrolling through body while sidenav is open
        $("body").css('overflow', 'hidden');
      });
      
      $(".closebtn").click(function(){
        $(".overlay").css("display", "none");
        $(".sidebar").css("transform", "translateX(-100%)");
        // Allows user to scroll through body after closing sidenav
         $("body").css('overflow', 'visible');
      });
      
      $(".overlay").click(function(){
          $(".overlay").css("display", "none");
        $(".sidebar").css("transform", "translateX(-100%)");
         // Allows user to scroll through body after closing sidenav
        $("body").css('overflow', 'visible');
      });

// https://www.codexworld.com/add-remove-input-fields-dynamically-using-jquery/

    var maxField = 30; //Input fields increment limitation
    var addButton = $('.add_button'); //Add button selector
    var wrapper = $('.field_wrapper'); //Input field wrapper
    var x = 1; //Initial field counter is 1
    var maxField2 = 30; //Input fields increment limitation
    var addButton2 = $('.add_button2'); //Add button selector
    var wrapper2 = $('.field_wrapper2'); //Input field wrapper
    var y = 1; //Initial field counter is 1

    //Once add button is clicked
    $(addButton).click(function(){
        //Check maximum number of input fields
        if(x < maxField){ 
            x++; //Increment field counter
            $(wrapper).append('<div><textarea class="form-control reduce" name="recipe_ingredient" rows="1" placeholder="Enter ingredient"></textarea><a href="#" class="remove_button">&#10008;</a></div>'); //Add field html
          
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
            $(wrapper2).append('<div><textarea class="form-control reduce" name="recipe_step" rows="2" placeholder="Enter step"/><a href="#" class="remove_button2">&#10008;</a></div>'); //Add field html
        }
    });
    
    //Once remove button is clicked
    $(wrapper2).on('click', '.remove_button2', function(e){
        e.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });
    
    // w3schools code
    
    var prevScrollpos = window.pageYOffset;
    $(window).on('scroll', function(){
    var currentScrollPos = window.pageYOffset;
    /*
    If the user scrolls down the page area, the menu disappears.
    Scrolling up off the page is not recognised to keep the menu
    fixed at the top when the user is viewing that area of the page.
    The menu reappears on scroll up. 
    */
    if (prevScrollpos > currentScrollPos || prevScrollpos <= 0) {
    $(".navbar-wrapper").css('top',"0");
        } else {
            $(".navbar-wrapper").css('top', "-70px");
                }
        prevScrollpos = currentScrollPos;
        }
    );
});

// D3/DC Code

queue()
.defer(d3.json, "/data")
.await(myTag)
.await(makeGraph);

// function found on stackoverflow 
function myTag(key, endAngle, startAngle){
    var percentage = dc.utils.printSingleValue((endAngle - startAngle) / (2*Math.PI) * 100);
    // hide tag is less than 5% of the chart to prevent labels from overlapping
    if (percentage > 5){
        return key + "(" + Math.round(percentage) + '%)';
        }
    }
 
function makeGraph(error, myDataJson) {
    var ndx = crossfilter(myDataJson);
        
    var type_dim = ndx.dimension(dc.pluck('Type'));
    var amount =  type_dim.group().reduceSum(dc.pluck('Amount'));
            
    dc.pieChart('#chart-here')
        .height(280)
        .width(280)
        .radius(120)
        .transitionDuration(1500)
        .dimension(type_dim)
        .group(amount)
        // function found on stackoverflow 
        .on('pretransition', function(chart){
            chart.selectAll('text.pie-slice').text( function(d) {
            return myTag(d.data.key, d.endAngle, d.startAngle);
            });
        });
                
    var views = type_dim.group().reduceSum(dc.pluck('Views'));
    dc.pieChart('#another-chart-here')
        .height(280)
        .width(280)
        .radius(120)
        .transitionDuration(1500)
        .dimension(type_dim)
        .group(views)
        .on('pretransition', function(chart){
        chart.selectAll('text.pie-slice').text( function(d) {
            return myTag(d.data.key, d.endAngle, d.startAngle);
            });
        });
             
                
    var favourites = type_dim.group().reduceSum(dc.pluck('Favourites'));  
    dc.pieChart('#final-chart-here')
        .height(280)
        .width(280)
        .radius(120)
        .transitionDuration(1500)
        .dimension(type_dim)
        .group(favourites)
        .on('pretransition', function(chart){
            chart.selectAll('text.pie-slice').text( function(d) {
            return myTag(d.data.key, d.endAngle, d.startAngle);
            });
        });
    
    dc.renderAll();
}

(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

// https://getbootstrap.com/docs/4.0/components/forms/#validation

