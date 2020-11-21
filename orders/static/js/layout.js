// Temporary pop-up informing users about any changes due to COVID-19/stay-at-home orders (only once per session)
document.addEventListener('DOMContentLoaded', function() {
  if (sessionStorage.getItem('covid-alert') === null) {
    Swal.fire({
      title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200; font-size: 24px;">UPDATE: as of April 6th, 2020...</span>',
      html: '<div style="color: #58483A; font-family: Caslon; font-weight: 200; font-size: 16px;">Following the recommended curfew set forth by Mayor Walsh, Pinocchio\'s will now be closing every night at 9:00pm. All orders must be takeout, but feel free to order inside or call ahead; we will continue taking orders until 8:00pm. Stay safe, wash your hands, maintain social distance, and always remember: EAT MORE PIZZA!</div>',
      background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
      height: '800px;'
    });
    sessionStorage.setItem('covid-alert', 'no');
  };
});

// MAY KEEP THIS IF WE WANWT TO HAVE ACTIVE NAV-HEADER STYLIZED
//$(document).ready(function() {
  //$("[href]").each(function() {
    //if (this.href == window.location.href) {
      //$(this).addClass('active-nav');
    //};
  //});
//});
