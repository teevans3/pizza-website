// Alert the user the username chosen is invalid/taken
Swal.fire({
  icon: 'error',
  title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Username taken.</span>',
  background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
});

// Remove all default Django errors
var errors = document.querySelectorAll('.errorlist');
for (var i = 0; i < errors.length; i++) {
  error[i].remove();
};
