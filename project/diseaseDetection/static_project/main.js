$(document).ready(function(){
    console.log("hello world");
    $("#popup-modal-btn").click(function(){
        console.log("btnclick");
        $('.ui.modal')
        .modal('show');
    });


    //for content edit remove and update option
    let display= false
    $(".display-menu").click(function(){
        console.log("bibash");
        $(".content-menu").show();
        if(display===false){

            $(this).next(".content-menu").show("slow");
            display=true;
        }
        else{
            $(this).next(".content-menu").hide("slow");
            display=false;
        }

    })





})