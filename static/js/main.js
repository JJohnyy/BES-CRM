

$(document).ready(function () {
    $('.navbar-link').click(function () {
        $('.navbar-link').removeClass("active");
        $(this).addClass("active");
    });
});


$(document).ready(function () {
    $('.lead-detail-link-item').click(function () {
        // Removing class from all list elements
        $('.lead-detail-link-item').removeClass('active');
        // Adding class to clicked list element
        $(this).addClass('active');
    });
});




$(function () {
    count = 0;
    wordsArray = ["BES CRM", "Bohemian Esteates", 'BES'];
    setInterval(function () {
        count++;
        $("#heading").fadeOut(400, function () {
            $(this).text(wordsArray[count % wordsArray.length]).fadeIn(600);
        });
    }, 2000);
});