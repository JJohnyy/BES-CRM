

$('.lead-detail-links-wrapper').on('click', '.lead-detail-link-item', function () {
    $('.lead-detail-link-item').removeClass('active');
    $(this).addClass('active');
});



$(function () {
    count = 0;
    wordsArray = ["BES CRM", "Bohemian Esteates"];
    setInterval(function () {
        count++;
        $("#heading").fadeOut(400, function () {
            $(this).text(wordsArray[count % wordsArray.length]).fadeIn(400);
        });
    }, 2000);
});