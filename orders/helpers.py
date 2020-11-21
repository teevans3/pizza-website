from django.contrib.auth.models import User
from .models import Pizza, Topping, Sub, SubTopping, Pasta, Salad, DinnerPlatter, Order, Item
import decimal



# Calculating a user's total in their cart/future order
def calc_total(cart_items):

    total_price = 0
    for item in cart_items:
        total_price += item.price

    return total_price


# Updating price of sub depending on toppings/extras ($0.50 ea)
def update_price(toppings_list, price):

    if len(toppings_list) < 1:
        price = price
    else:
        for topping in toppings_list:
            price += decimal.Decimal(0.5)

    return price


# Organizing platters (rearrange them by type: salad or pasta platter) for the menu page
def organize_platters():

    salad_platters = DinnerPlatter.objects.filter(name__icontains='Salad').order_by('smallprice')
    other_platters = DinnerPlatter.objects.exclude(name__icontains='Salad').order_by('smallprice')
    platters = list(salad_platters) + list(other_platters)

    return platters


# Formatting toppings as string (for display purposes)
def format_toppings(toppings_list):

    if len(toppings_list) < 1:
        toppings = "None"
    else:
        toppings = ""
        for topping in toppings_list:
            if len(toppings_list) == 1:
                toppings += topping
            else:
                if topping == toppings_list[-1]:
                    toppings += ("& " + topping)
                else:
                    toppings += (topping + ", ")

    return toppings


# Formatting items for displaying in their cart (both on orders page and admin page)
def format_items(user, name, toppings_list, type, size_price):

    # Create a new item object (to be added to their cart)
    item = Item()
    # Add all relevant info to the item model
    item.user = user
    item.name = name
    # Default order number (0) for all items until order is actually placed
    item.order_number = 0
    item.toppings = format_toppings(toppings_list)
    # For Pizza, Sub, and Platter, size_price = "size;price"
    if (type != "Pasta") and (type != "Salad"):
        # Split up string because size and price were sent together
        list = size_price.split(';')
        item.size = list[0]
        if type == "Sicilian" or type == "Regular":
            item.type = (type + " Pizza")
            item.price = list[1]
        elif type == "Platter":
            item.type = ("Dinner " + type)
            item.price = list[1]
        else:
            item.type = type
            # Update Sub price to include toppings/extras ($0.50 ea)
            price = decimal.Decimal(list[1])
            item.price = update_price(toppings_list, price)
    # For Pasta and Salad, there is only one size; as such, size_price = "price"
    else:
        item.type = type
        item.size = "NA"
        item.price = size_price
    # Save item to database
    item.save()


# Placing an order when user checks out
def place_order(user, cart_items, total_items, total_price):

    # Create a new order object (match order_number with items' order_numbers)
    new_order = Order()
    # Assign order number based on the length of total orders (may not account for race conditions??)
    order_number = len(Order.objects.all())
    # Add all relevant info to the order model
    new_order.user = user
    new_order.number = order_number
    new_order.total_items = total_items
    new_order.total_price = total_price
    # A string of all items in the order (formatted for display/legiblity purposes)
    all_items = ""
    for item in cart_items:
        if item.size == "NA":
            all_items += f"Item ID: {item.id}.....{item.name}..........${item.price} \n"
        elif item.type == "Dinner Platter":
            all_items += f"Item ID: {item.id}.....{item.size} {item.name} {item.type}..........${item.price} \n"
        else:
            all_items += f"Item ID: {item.id}.....{item.size} {item.name} {item.type} (Toppings: {item.toppings})..........${item.price} \n"
    new_order.all_items = all_items
    new_order.save()
    
    # Change status from "in cart" to "in order" and update order_number to match its respective order
    for item in cart_items:
        item.status = "IN ORDER"
        item.order_number = order_number
        item.order = new_order
        item.save()
