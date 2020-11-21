# Project 3

Web Programming with Python and JavaScript


I decided to go all-out for this project, since it's the final one, and create a complete website for Pinocchio's Pizza to take orders online. All of the information written on this website is pulled from the original Pinocchio's Pizza website (though I did tweak some of the sentences in order to have a better flow).

Layout.html contains the base/layout for the entire website, including a navigation bar (slightly different if a user is logged in or not) and a footer (containing basic information about restaurant as well as links to their social media).

Index.html is the homepage for the website, containing a slider of various pizzas and restaurant images (all random, arbitrarily-chosen images), information about the restaurant, the YouTube videos containing the mentions, and the different options users can use to order from Pinocchio's.

Menu.html contains all of the items on Pinocchio's menu as well as pictures for each type of item (pizza, sub, etc.). It is also accommodating for the possibility of future items to be added. User's are prohibited from adding items if they are not logged in.

Orders.html contains a list of all items in the user's cart (if they have any), an option to remove items, a picture of each item, and the total price (next to the check-out button). It also contains all the past orders (including they're most recently-placed order), including the status of the order (pending, cooking, etc.), all items within the order, and the price. This page can only be viewed if a user is logged in.

Account.html contains information about the user (username, full name, email, address, option to change password, and a log-out button).  The change-password link directs the user to Change_password.html which has a form for the user to change their password. An alert will pop up if there was an error with the form. Both of these pages can only be viewed if a user is logged in.

About.html contains information about Pinocchio's Pizza, which includes contact information, the location, and hours of operation.

Login.html contains a form for the user to log in. An alert will pop up if there is an error with the form.

Register.html contains a form for the user to register for an account. An alert will pop up if there is an error with the form.

Styles.css contains all of the css/styling code for the entire project. I have organized it by hierarchy of importance, relative to each html file. This file may be excessive, as I am still learning how to better condense my css and perfect the formatting etiquette.

I decided to breakdown all Javascript code into different files (not sure if this was a smart move, but I thought it would be better to keep it organized this way). As such, index.js contains the JS code for index.html, menu_anon.js contains the JS code for the menu when a user is not signed in, menu_user.js contains the JS code for the menu when a user is signed in, etc.

Views.py contains the functions for handling each page in this project.

Helpers.py contains the functions used within views.py to better display information from the database as well as better display information collected from a user's form on the admin page.

Forms.py contains the forms in which users create an account and change their password.

Models.py contains all of my models used for this project. These include models for the different types of menu items (pizza, subs, etc.; toppings and sub-toppings have their own models) as well as models for the Item (which I have classified as when a user adds something to their cart, it becomes an item; such as a Small 2 Topping Pizza with Mushrooms and Onions). The Item model has a status of either "in cart" or "in order" (because an item doesn't exist until a user has claimed it by either adding it to their cart or adding it to an order). Once a user checks out/places their order, the status of the item(s) associated with that order is changed to "in order" and an order ID is assigned to that order. The Order model also contains a status of the progress of the order (pending, cooking, delivering, etc.) which the admins can manually update (which will then update on the user's order history section). Each order, when clicked on in the admin page, is adjusted to easily see each item contained within the order (including the ID associated with each item).

I also wanted to point out the plugins I used: JQuery's Chosen for stylizing the select box (for toppings); SweetAlert2 for stylizing pop-ups/alerts (though I couldn't figure out how to turn off the default auto-focus on the confirm buttons...); SlickCarousel for the slider/carousel images; and Google fonts.

There were some drawbacks I had with this project: 1) I was able to adjust the contents relative to the width of the web-screen using media queries... but for some pages, however, the height of the page would increase drastically (even though no elements existed that far down on the page) and thus the footer would not be placed at the bottom. 2) Sometimes the slider images don't switch unless the window is unfocused (luckily, they worked in the video; hopefully this is just due to the plugin I used). 3) I have a bunch of different, very small, JS files. The main reason for this is because I couldn't figure out how to detect whether a user was signed in via JS (so instead I checked through the relevant html files using Jinja). I implemented this multiple times.. such as when checking what type of error the user had when registering for an account and then calling the appropriate JS file. I know there is a better way to do this but with only one JS file, but I could not figure it out (I'm assuming I'd have to use Ajax or JQuery or both?). 4) I don't think my CSS code and use of class names, IDs, etc. were as efficient as they could be. 5) When adding more than one topping to an item, the Chosen select box would increase in height, resulting in stretching the entire table's height (which can look pretty awful). I could not figure out how to, rather than increase the height when toppings are added, increase the width instead... or even have the box's dimensions not increase at all and have an automatic scrolling bar/overflow horizontally.
