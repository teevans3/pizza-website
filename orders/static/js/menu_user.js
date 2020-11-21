// If user is logged in, allow them to add items to their cart
var addbtns = document.querySelectorAll('.add-item');
addbtns.forEach(function(btn) {
  btn.addEventListener('click', function(event) {
    // Prevent user from submitting form if incomplete
    event.preventDefault();
    var itemInfo = btn.id;
    var itemForm = document.getElementsByName(itemInfo)[0];
    if (itemForm.checkValidity()) {
      // Alert the user that their item was added to the cart
      Swal.fire({
        icon: 'success',
        title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Item added to cart!</span>',
        background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
      }).then((result) => {
        itemForm.submit();
      });
    } else {
      // Alert the user that their form is incomplete (size and/or toppings not chosen)
      var sizeRadios = itemForm.parentElement.querySelectorAll('.size-radio');
      var checkedRadios = 0;
      console.log(sizeRadios);
      for (var i = 0; i < sizeRadios.length; i++) {
        if (sizeRadios[i].checked) {
          checkedRadios += 1;
        };
      };
      if (checkedRadios < 1) {
        console.log("pick a size")
        Swal.fire({
          icon: 'error',
          title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Please pick a size.</span>',
          background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
        });
      } else {
        Swal.fire({
          icon: 'error',
          title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Please choose your topping(s).</span>',
          background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
        });
      }
    };
  });
});
