window.onload = function() {
    const heightBody = document.body.offsetHeight;
    document.getElementById('logo-site').style.height = document.body.offsetHeight * 55 / 100 + 'px';
};

var $doc = $('html, body');
$('.jsNavbar').click(function() {
    document.getElementById('navbar-mobile').classList.toggle('active');
    document.getElementById('navbar-menu').classList.toggle('deactive');
});

var $doc = $('html, body');
$('.jsNavbarClose').click(function() {
    document.getElementById('navbar-mobile').classList.toggle('active');
    document.getElementById('navbar-menu').classList.toggle('deactive');
});

var $doc = $('html, body');
$('.jsNavMobile').click(function() {
    document.getElementById('navbar-mobile').classList.toggle('active');
    document.getElementById('navbar-menu').classList.toggle('deactive');
});

var $doc = $('html, body');
$('.scrollSuave').click(function() {
    $doc.animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});
