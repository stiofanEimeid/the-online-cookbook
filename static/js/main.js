

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
                .height(330)
                .radius(90)
                .transitionDuration(1500)
                .dimension(type_dim)
                .group(amount);
                
           
            var views =  type_dim.group().reduceSum(dc.pluck('Views'));
            dc.pieChart('#another-chart-here')
                .height(330)
                .radius(90)
                .transitionDuration(1500)
                .dimension(type_dim)
                .group(views);

        dc.renderAll();
};
  
     
         
         

$(document).ready(function(){

  $(".fadeMe1").each(function(i) {
  $(this).animate({'opacity':'1'},3000);
});

// intro fadeIn (tcloniger code)
    
    /* Every time the window is scrolled ... */
    $(window).scroll( function(){
    
        /* Check the location of each desired element */
        $('.fadeMe2').each( function(i){
            
            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            /* If the object is completely visible in the window, fade it it */
            if( bottom_of_window > bottom_of_object ){
                
                $(this).animate({'opacity':'1'},3000);
                    
            }
            
        }); 
    
    });
    
     
 
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

