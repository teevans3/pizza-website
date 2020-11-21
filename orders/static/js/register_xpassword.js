// Alert the user there is an error with their password
Swal.fire({
  icon: 'error',
  title: '<span style="color: #58483A; font-family: Caslon; font-weight: 200">Your password must:</span>',
  html: '<div style="color: #58483A; font-family: Caslon; font-weight: 200; font-size: 16px;"><ul style="text-align: left; margin-left: 150px; margin-right: 120px;"><li>Be unique</li><li>Contain at least 8 characters</li><li>Consist of at least one letter and one number</li><li>Passwords must match</li></ul></div>',
  background: 'linear-gradient(50deg, #ffffff, #e5e5e5, #cccccc)',
});

// Remove all default Django errors
var errors = document.querySelectorAll('.errorlist');
for (var i = 0; i < errors.length; i++) {
  error[i].remove();
};
