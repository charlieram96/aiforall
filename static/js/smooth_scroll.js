$("#button1").click(function() {
    $('html, body').animate({
        scrollTop: $("#plan").offset().top
    }, 1000);
});