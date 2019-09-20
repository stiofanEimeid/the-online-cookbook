/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector(".navbar-wrapper").style.top = "0";
  } else {
    document.querySelector(".navbar-wrapper").style.top = "-70px";
  }
  prevScrollpos = currentScrollPos;
};

// Credit: https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp
     queue()
    .defer(d3.json, "/data")
    .await(makeGraph);
 
    
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
                .on('pretransition', function(chart){
                    chart.selectAll('text.pie-slice').text( function(d) {
                    return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
                    });
                });
                
                // https://stackoverflow.com/questions/25209971/add-percentages-to-the-pie-chart-label-in-dc-js
                
                
                
            var views =  type_dim.group().reduceSum(dc.pluck('Views'));
            dc.pieChart('#another-chart-here')
                .height(280)
                .width(280)
                .radius(120)
                .transitionDuration(1500)
                .dimension(type_dim)
                .group(views)
                .on('pretransition', function(chart){
                    chart.selectAll('text.pie-slice').text( function(d) {
                    return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
                    });
                })
                ;
             
                
            var favourites =  type_dim.group().reduceSum(dc.pluck('Favourites'));  
            dc.pieChart('#final-chart-here')
                .height(280)
                .width(280)
                .radius(120)
                .transitionDuration(1500)
                .dimension(type_dim)
                .group(favourites)
                on('pretransition', function(chart){
                    chart.selectAll('text.pie-slice').text( function(d) {
                    return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
                    });
                });
                
     
            

        dc.renderAll();
}


  
$(document).ready(function(){
    
$('#myTooltip').tooltip();

$('#mySecondTooltip').tooltip();

     var back = ["#90CCF4", "#f78888", "#f3d250"];
     
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
      
    //   overlay only displayed when sidebar selected
       $(".openbtn" ).click(function(){
        $(".overlay").css("display", "block")
        $(".sidebar").css("transform", "translateX(0%)")
        // Push content over
        $("body").css('overflow', 'hidden')
      });
      

      $(".closebtn").click(function(){
        $(".overlay").css("display", "none")
        $(".sidebar").css("transform", "translateX(-100%)")
        // Push content back
         $("body").css('overflow', 'visible')
     
      });
      
      $(".overlay").click(function(){
          $(".overlay").css("display", "none")
        $(".sidebar").css("transform", "translateX(-100%)")
        // Push content back
        $("body").css('overflow', 'visible')
         $(".content, .navbar, .footer").addClass("untranslateMe")
         $(".content, .navbar, .footer").removeClass("translateMe")
       
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
            $(wrapper).append('<div><textarea class="form-control reduce" name="recipe_ingredient" rows="1" value="" placeholder="Ingredient"></textarea><a href="#" class="remove_button">&#10008;</a></div>'); //Add field html
          
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
            $(wrapper2).append('<div><textarea class="form-control reduce" name="recipe_step" rows="2" value="" placeholder="Step"/><a href="#" class="remove_button2">&#10008;</a></div>'); //Add field html
        }
    });
    
    //Once remove button is clicked
    $(wrapper2).on('click', '.remove_button2', function(e){
        e.preventDefault();
        $(this).parent('div').remove(); //Remove field html
        x--; //Decrement field counter
    });
 
});

