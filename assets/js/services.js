$(document).ready(function(){
    $('.services-slick').slick({
        centerMode: true,
        slidesToShow: 4,
        arrows: true,
        dots: true,
        prevArrow: '.services-button-prev',
        nextArrow: '.services-button-next',
        responsive: [
            {
              breakpoint: 1050,
              settings: {
                slidesToShow: 3,
              }
            },
            {
              breakpoint: 900,
              settings: {
                slidesToShow: 2,
                arrows: false,
              }
            },
            {
                breakpoint: 630,
                settings: {
                  slidesToShow: 1,
                  arrows: false,
                }
              }
          ]
    });
});