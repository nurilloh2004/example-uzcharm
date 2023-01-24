$(window).on('load', function () {
    if ($('#preloader').length) {
        $('#preloader').delay(600).fadeOut('slow', function () {
            $(this).remove();
        });
    }
});

$(document).ready(function () {


    $("h1, p").delay("1000").fadeIn();


    $("#back-top").hide();


    $(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() > 200) {
                $('#back-top').fadeIn();
            } else {
                $('#back-top').fadeOut();

            }
        });


        $('a#back-top').click(function () {
            $('body,html').animate({
                scrollTop: 0
            }, 200);
            return false;
        });
    });


});

$('.usefull-site-carousel').owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    dots: false,
    lazyLoad: !0,
    autoplay: !0,
    autoplayTimeout: 6e3,
    autoplayHoverPause: !0,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        700: {
            items: 2
        },
        1000: {
            items: 4
        }
    }
});


$('.list-header').on('click', function () {
    var $J_li = $(this).parents('.J_list')
    $J_li.hasClass('open') ? $J_li.removeClass('open') : $J_li.addClass('open');
});

$('.partner-carousel').owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    dots: false,
    lazyLoad: !0,
    autoplay: !0,
    autoplayTimeout: 6e3,
    autoplayHoverPause: !0,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        700: {
            items: 2
        },
        1000: {
            items: 4
        }
    }
});

$('.products-carousel').owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    dots: false,
    lazyLoad: !0,
    autoplay: !0,
    autoplayTimeout: 6e3,
    autoplayHoverPause: !0,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        700: {
            items: 2
        },
        1000: {
            items: 4
        }
    }
});

$('.new-carousel').owlCarousel({
    loop: false,
    margin: 10,
    nav: true,
    dots: false,
    lazyLoad: !0,
    autoplay: !0,
    autoplayTimeout: 6e3,
    autoplayHoverPause: !0,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        700: {
            items: 2
        },
        1000: {
            items: 3
        }
    }
});

$('.about-carousel').owlCarousel({
    loop: false,
    margin: 10,
    nav: false,
    dots: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});


$("#vmap path").on("click", function (e) {
    e.preventDefault();
    $(".map-title").text($(this).data('city'));
    $('.map-phone').text($(this).data('phone'));
    $(".map-title").show();
});

$("#vmap path").on("mouseout", function () {
    $("#vmap-tooltip").hide();
});

if ($("#tilt").length) {

    //  img hover
    let el = document.getElementById('tilt')

    const height = el.clientHeight
    const width = el.clientWidth
    el.addEventListener('mousemove', handleMove)


    function handleMove(e) {

        const xVal = e.layerX

        const yVal = e.layerY

        const yRotation = 20 * ((xVal - width / 2) / width)

        const xRotation = -20 * ((yVal - height / 2) / height)

        const string = 'perspective(500px) scale(1.1) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg)'

        el.style.transform = string
    }

    el.addEventListener('mouseout', function () {
        el.style.transform = 'perspective(500px) scale(1) rotateX(0) rotateY(0)'
    });


    el.addEventListener('mousedown', function () {
        el.style.transform = 'perspective(500px) scale(0.9) rotateX(0) rotateY(0)'
    });

    el.addEventListener('mouseup', function () {
        el.style.transform = 'perspective(500px) scale(1.1) rotateX(0) rotateY(0)'
    });

}


document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            document.getElementById('navbar_top').classList.add('fixed-top');
            navbar_height = document.querySelector('.navbar').offsetHeight;
            document.body.style.paddingTop = navbar_height + 'px';
        } else {
            document.getElementById('navbar_top').classList.remove('fixed-top');
            document.body.style.paddingTop = '0';
        }
    });
});


if ($('.search-popup__toggler').length) {
    $('.search-popup__toggler').on('click', function (e) {
        $('.search-popup').addClass('active');
        e.preventDefault();
    });
}

if ($('.search-popup__overlay').length) {
    $('.search-popup__overlay').on('click', function (e) {
        $('.search-popup').removeClass('active');
        e.preventDefault();
    });
}

$("#jqvmap1_item12").click();