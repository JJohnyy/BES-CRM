
$(function () {
    count = 0;
    wordsArray = ["BES CRM", "Bohemian Estates", "BES"];
    setInterval(function () {
        count++;
        $("#heading").fadeOut(400, function () {
            $(this).text(wordsArray[count % wordsArray.length]).fadeIn(600);
        });
    }, 2000);
});