document.addEventListener("DOMContentLoaded", function() {
  // Image slider for homepage
  $(document).ready(function(){
    $('.slider').slick({
      slidesToShow: 1,
      infinite: true,
      fade: true,
      autoplay: true,
      speed: 4000,
      autoplaySpeed: 4000
    });
  });
});
