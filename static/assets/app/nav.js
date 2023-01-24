const overlay = document.getElementById('overlay');

const closeM = document.getElementById('close');

const openM = document.getElementById('open');

openM.addEventListener('click', function () {
    overlay.classList.add('show1');
    document.querySelector('html').style.overflowY = 'hidden';
});

closeM.addEventListener('click', function () {
    overlay.classList.remove('show1');
    document.querySelector('html').style.overflowY = 'scroll';
});


document.querySelector('.pooreye').addEventListener('click', (e) => {
    e.preventDefault();
    document.querySelector("html").classList.toggle("filter");
});

$('#plus').on('click', function () {
    $('h1, h2, h3, h4, h5, h6, p, a, span').animate({'font-size': '+=1'}, 1);
});

$('#minus').on('click', function () {
    $('h1, h2, h3, h4, h5, h6, p, a, span').animate({'font-size': '-=1'}, 1,);
});

$('#reset').on('click', function () {
    $('h1, h2, h3, h4, h5, h6, p, a, span').removeAttr('style');
});

$("[data-trigger]").on("click", function () {
    var trigger_id = $(this).attr('data-trigger');
    $(trigger_id).toggleClass("show");
    $('body').toggleClass("offcanvas-active");
});

$(".btn-close").click(function (e) {
    $(".navbar-collapse").removeClass("show");
    $("body").removeClass("offcanvas-active");
});

jQuery(document).ready(function() {

    var mouseX = 0, mouseY = 0;
    var xp = 0, yp = 0;

    $(document).mousemove(function(e){
        mouseX = e.pageX - 30;
        mouseY = e.pageY - 30;
    });

    setInterval(function(){
        xp += ((mouseX - xp)/6);
        yp += ((mouseY - yp)/6);
        $("#circle").css({left: xp +'px', top: yp +'px'});
    }, 20);

});