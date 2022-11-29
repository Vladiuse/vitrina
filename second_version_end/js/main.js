$(function () {

  $('.menu').on('click', function () {
    $('.menu-list').slideToggle();
    $('.menu__close').slideToggle();
  });

  $(function () {
    $(window).scroll(function () {
      if ($(this).scrollTop() != 0) {
        $('#toTop').fadeIn();
      } else {
        $('#toTop').fadeOut();
      }
    });

    $('#toTop').click(function () {
      $('body,html').animate({ scrollTop: 0 }, 800);

    });

  });

});