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

    //for ajax like without reloading
    //for ajax like and unlike without reloading
    $('.like-form').submit(function(e){
        e.preventDefault()
        const post_id = $(this).attr('id')

        const bibash = $(`.like-btn${post_id}`)
        const happy = $.trim(bibash) 
        console.log(happy)
        console.log(bibash)
       

        const likeText = $(`.like-btn${post_id}`).text()
        const trim = $.trim(likeText)
        
        

        const url = $(this).attr('action')
        

        let res;
        const likes = $(`.like-count${post_id}`).text()
        const trimcount = parseInt(likes) 
        
        

       $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,   
            },
            success: function(response){
                if(trim === 'Unlike'){
                   const likes = $(`.like-btn${post_id}`).text('Like')
                   res = trimcount - 1 ;
                }
                else{
                   const likes = $(`.like-btn${post_id}`).text('Unlike')
                   res = trimcount + 1 ;
                }
                $(`.like-count${post_id}`).text(res)
            },
            error: function(response){
                console.log('error', response)
            }
       }) 
   });

    // for ajax comment without reloading adding comment
    $('.comment-form').submit(function(e){
        e.preventDefault();
        console.log("working")


        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id,   
            },
        
        
    });






})