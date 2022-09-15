// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function() {
    $('.filters_menu li').click(function() {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
});

/** google_map js **/
// function myMap() {
//     var map = L.map('map').setView([0, 0], 1);

//     L.tileLayer('https://api.maptiler.com/maps/streets-v2/{z}/{x}/{y}.png?key=b8Puymxn2SFp25xNDbWu', {
//         tileSize: 512,
//         zoomOffset: -1,
//         minZoom: 1,
//         attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
//         crossOrigin: true
//     }).addTo(map);
//     var marker = L.marker([34.26009687946747, -6.562222298228314]).addTo(map);
// }
// myMap();
// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});