// Switch between menus without reloading page (pizzas, subs, pastas & salads, platters)
var titles = document.querySelectorAll('.menu-title');
titles.forEach(function (title) {
  title.addEventListener('click', function() {
    // Untoggle all currently "active" titles
    for (var i = 0; i < titles.length; i++) {
      if (titles[i].parentNode.classList.contains('active-title')) {
        titles[i].parentNode.classList.toggle('active-title');
      };
    };
    // Toggle new "active" title
    event.target.parentNode.classList.toggle('active-title');
    // TODO: remove currently "active" menu from display
    var sections = document.querySelectorAll('.menu-section');
    for (var i = 0; i < sections.length; i++) {
      if (sections[i].classList.contains('active')) {
        sections[i].classList.toggle('active');
      };
    };

    // Display "active" menu
    if (document.getElementById('pizzas-title').classList.contains('active-title')) {
      document.getElementById('pizzas').classList.toggle('active');
    };
    if (document.getElementById('subs-title').classList.contains('active-title')) {
      document.getElementById('subs').classList.toggle('active');
    };
    if (document.getElementById('pastas-salads-title').classList.contains('active-title')) {
      document.getElementById('pastas-salads').classList.toggle('active');
    };
    if (document.getElementById('platters-title').classList.contains('active-title')) {
      document.getElementById('platters').classList.toggle('active');
    };
  });
});

// Jquery "Chosen" plugin for styling dropdown for pizza and subs toppings
var pizzatoppings = document.querySelectorAll('.pizzatoppings');
for (var i = 0; i < pizzatoppings.length; i++) {
    if (pizzatoppings[i].classList.contains('1')) {
      $('.1').chosen({
        disable_search: true,
        max_selected_options: 1,
        width: "115px",
      });
    };
    if (pizzatoppings[i].classList.contains('2')) {
      $('.2').chosen({
        max_selected_options: 2,
        width: "115px",
        disable_search: true,
      });
    };
    if (pizzatoppings[i].classList.contains('3')) {
      $('.3').chosen({
        max_selected_options: 3,
        width: "115px",
        disable_search: true,
      });
    };
  };
$(".subtoppings").chosen({
  max_selected_options: 4,
  width: "115px",
  disable_search: true,
});
