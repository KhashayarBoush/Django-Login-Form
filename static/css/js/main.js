$(document).ready(function(){
    $("#login").click(function(){
    var username = $("#username").val();
    var password = $("#password").val();
    // Checking for blank fields.
    if( username =='' || password ==''){
    $('input[type="text"],input[type="password"]').css("border","2px solid red");
    $('input[type="text"],input[type="password"]').css("box-shadow","0 0 3px red");
    alert("همه ی فیلد ها را پر کنید");
    }
    });
    });