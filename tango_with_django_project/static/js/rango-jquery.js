$(document).ready(function(){
    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
    $("p").hover( function(){
        $(this).css('color', 'green');
    },
    function(){
        $(this).css('color', 'black');
    });
    $('#about-btn').click( function(event) {
        $(this).removeClass('btn-ptimary').addClass('btn-success');
    });
    $('#about-btn').click( function(event) {
       text = $("#msg").html()
       text = text + "oOO"
       $("#msg").html(text)
    });
});