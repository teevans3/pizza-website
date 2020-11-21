// Alert user to make sure they are ready to check out, if their cart is not empty
var cartItems = document.querySelectorAll('.cart-item');
if (cartItems.length > 0) {

  var checkout = document.getElementById('checkout');
  var totalPrice = document.querySelector('#total-price').innerHTML;

  checkout.addEventListener('click', function(event) {
    event.preventDefault();
    Swal.fire({
      icon: 'question',
      showCancelButton: true,
      confirmButtonText: 'Yes, place my order',
      cancelButtonText: 'No, I\'m not ready',
      title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Ready to check out?</span>',
      html: '<div style="color: #58483A; font-family: Caslon; font-weight: 200; font-size: 20px;">Total: ' + totalPrice + '</div>',
      background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
    }).then((result) => {
        if (result.value) {
          Swal.fire({
            icon: 'success',
            confirmButtonText: 'OK',
            title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Your order has been placed!</span>',
            html: '<div style="color: #58483A; font-family: Caslon; font-weight: 200; font-size: 16px;">View your order\s status in the right-hand Order History column.</div>',
          }).then((result) => {
            document.getElementById('checkout-form').submit();
          });
        };
    });
  });



  // FIX THIS: GLITCH WHERE REMOVING ITEMS REMOVES FIRST ITEM

  // Also allow the user to remove items from their cart
  var removebtns = document.querySelectorAll('.remove-item');
  console.log(removebtns);
  removebtns.forEach(function(btn) {
    btn.addEventListener('click', function(event) {
      event.preventDefault();
      Swal.fire({
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Yes, remove it',
        cancelButtonText: 'No, keep it',
        title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Are you sure you want to remove this item?</span>',
        background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
      }).then((result) => {
          if (result.value) {
            itemID = btn.id;
            formID = (itemID + '-form');
            document.getElementById(formID).submit();
          };
      });
    });
  });
};


// If order is complete, change background color of past-order element
var pastorders = document.querySelectorAll('.orders-container');
var statuses = document.querySelectorAll('.status');
for (var i = 0; i < statuses.length; i++) {
  if(statuses[i].classList.contains('complete')) {
    pastorders[i].classList.toggle('orders-bg-2');
  } else {
    pastorders[i].classList.toggle('orders-bg-1');
  };
};
