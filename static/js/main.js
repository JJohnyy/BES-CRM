

$('.menu').on('click', '.lead-detail-link-item', function () {
    $('.lead-detail-link-item.active').removeClass('active');
    $(this).addClass('active');
});



$(function () {
    count = 0;
    wordsArray = [""];
    setInterval(function () {
        count++;
        $("#").fadeOut(400, function () {
            $(this).text(wordsArray[count % wordsArray.length]).fadeIn(400);
        });
    }, 2000);
});