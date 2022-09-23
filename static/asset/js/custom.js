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

// Modal
// Get the name
var name_ = document.getElementById("name");
var name_err = document.getElementById("name_err");
$(document).ready(function() {
    prep_modal();
    name_err.style.visibility = 'hidden';
});

function prep_modal() {
    $(".modal").each(function() {

        var element = this;
        var pages = $(this).find('.modal-split');

        if (pages.length != 0) {
            pages.hide();
            pages.eq(0).show();

            var b_button = document.createElement("button");
            b_button.setAttribute("type", "button");
            b_button.setAttribute("class", "btn btn-primary");
            b_button.setAttribute("style", "display: none;");
            b_button.innerHTML = "Back";

            var n_button = document.createElement("button");
            n_button.setAttribute("type", "button");
            n_button.setAttribute("class", "btn btn-outline-primary");
            n_button.innerHTML = "Next";

            $(this).find('.modal-footer').append(b_button).append(n_button);


            var page_track = 0;

            $(n_button).click(function() {

                this.blur();

                if (page_track == 0) {
                    $(b_button).show();
                }

                if (page_track == pages.length - 2) {
                    $(n_button).text("Checkout");
                }

                if (page_track == pages.length - 1) {
                    if (name_.value == "") {
                        name_err.style.visibility = 'visible';
                    } else {
                        name_err.style.visibility = 'hidden';
                        $(element).find("form").submit();
                    }
                }

                if (page_track < pages.length - 1) {
                    page_track++;

                    pages.hide();
                    pages.eq(page_track).show();
                }


            });

            $(b_button).click(function() {

                if (page_track == 1) {
                    $(b_button).hide();
                }

                if (page_track == pages.length - 1) {

                    $(n_button).text("Next");
                }

                if (page_track > 0) {
                    page_track--;

                    pages.hide();
                    pages.eq(page_track).show();
                }


            });

        }

    });
}

/* hide address_input if R_Pickup is selected */
var adress = document.getElementById("address_input");
var R_Pickup = document.getElementById("R_Pickup");
var R_Delivery = document.getElementById("R_Delivery");

R_Pickup.addEventListener("click", function() {
    adress.style.visibility = 'hidden';
});

R_Delivery.addEventListener("click", function() {
    adress.style.visibility = 'visible';
});