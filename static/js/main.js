$(document).ready(function(){
    var maxField = 12; //Input fields increment limitation
    var addButton = $('.add_button'); //Add button selector
    var wrapper = $('.field_wrapper'); //Input field wrapper
    var x = 1; //Initial field counter is 1
    var maxField2 = 12; //Input fields increment limitation
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

   $(window).on("load",function(){
         $(".loader-wrapper").fadeOut("slow");
    });