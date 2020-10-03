



$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});



function comment(iid){

comment = document.getElementById('comment').value;

$.ajax({url: '/blog-comments/'+iid+'/'+comment, success: function(result){
                var $tr = '';
               result.forEach((item) => {

                document.getElementById('comment').value= ""
                $("#blog_comment").append('<b style="color:#ff3300; text-transform: uppercase;">'+item.user__username+'</b>:<span style="font-size: small;">&nbsp &nbsp'+item.created_at+'&nbsp</span><span id="'+item.id+'"><a onclick="like_comment('+item.id+')"><i class="fas fa-thumbs-up">&nbsp'+item.like+'</i></a></span><p style= "padding-top: 8px;padding-left: 90px;"><span style="background-color: yellow;">'+item.comments+'</span></p><br>')
               });


}});

}


function like_comment(comment_id){

$.ajax({url: '/increase_like/'+comment_id, success: function(result){



 $('#'+comment_id).html('<span id='+comment_id+'><a onclick="like_comment('+comment_id+')"><i class="fas fa-thumbs-up">&nbsp'+result+'</i></a>')


}
});

}



