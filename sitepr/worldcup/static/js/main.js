var a= 0;
$(document).ready(function(){
    
     $('.message a').click(function(){
        $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
     });
     
//    $('.nav-login').click(function(){
//        $('.tte').css("display", "block");
//     });
    
    $('.nav-login').on('click touch',function(){
        $('.tte').css("display", "block");
     });
    
    $('.ttte').click(function(){
        $('.tte').css("display", "none");
     });
    

    
    
    
    
     $(".navbar__mobile").click(function(){
        if(a==0){
            $(".menu").slideDown("slow");
//            $( ".group__table" ).fadeTo( "slow" , 1, function() {
//    // Animation complete.
//  });
//             $( ".group__container" ).fadeTo( "slow" , 1, function() {
//    // Animation complete.
//  });
            a++;
        }else{
            $(".menu").slideUp("slow");
            a--;
        }
    
    });
    
    
});

function myFunction(){
    $('.tte').css("display", "block");
}

