// Don't allow user to add items to their cart if they are not logged in
var addItems = document.querySelectorAll('.add-item');
addItems.forEach(function(item) {
  item.addEventListener('click', function(event) {
    event.preventDefault();
    Swal.fire ({
      icon: 'error',
      title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Please log in to purchase items.</span>',
      background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
    }).then((result) => {
        window.location = "/login";
    });
  });
});
