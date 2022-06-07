

$(document).ready(function() {
    $(".lead-detail-link-item").click(function () {
        if(!$(this).hasClass('active'))
        {
            $(".lead-detail-link-item.active").removeClass("active");
            $(this).addClass("active");        
        }
    });
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