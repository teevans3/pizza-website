from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from orders.forms import RegistrationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user
from django.db.models import Q
from django.urls import reverse
from .models import Pizza, Topping, Sub, SubTopping, Pasta, Salad, DinnerPlatter, Order, Item
from .helpers import format_toppings, update_price, format_items, organize_platters, place_order, calc_total
import decimal



def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def menu(request):
    context = {
        "pizza_reg": Pizza.objects.filter(type__icontains='Regular').order_by('smallprice'),
        "pizza_sic": Pizza.objects.filter(type__icontains='Sicilian').order_by('smallprice'),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all().order_by('largeprice'),
        "subtoppings": SubTopping.objects.all(),
        "pastas": Pasta.objects.all().order_by('price'),
        "salads": Salad.objects.all().order_by('price'),
        # Organize platters (salad vs other)
        "platters": organize_platters()
    }
    return render(request, "menu.html", context)


@login_required(login_url="login")
def orders_view(request):
    user = request.user
    # Retrieve all items in a user's cart (including how many) and calculate the total price
    cart_items = Item.objects.filter(user__username__icontains=user).filter(status__icontains="IN CART")
    total_items = len(cart_items)
    total_price = calc_total(cart_items)

    if request.method == "POST":
        place_order(user, cart_items, total_items, total_price)
        return redirect("/orders")

    else:
        # Display all orders (past and current) as well as all the items within each order
        orders_list = Order.objects.filter(user__username__icontains=user).order_by('-number')
        items_list = Item.objects.filter(Q(status__icontains="IN ORDER") & Q(user__username__icontains=user)).order_by('-order_number')

        context = {
            "user": user,
            "cart_items": cart_items,
            "total_price": total_price,
            "total_items": total_items,
            "orders_list": orders_list,
            "items_list": items_list,
            # Determin if orders display is empty or not
            "orders_len": len(orders_list)
        }

        return render(request, "orders.html", context)


@login_required(login_url="login")
def account(request):
    if request.method == "GET":
        return render(request, "account.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            register_message = "registration failure"
            return render(request, "register.html", {"form": form, "register_message": register_message})
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    # Figure out how to redirect user to last page visited before logging in
    # See the net ninja's - "django tutorial #25 redirecting after login"
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {"login_message":"Invalid credentials."})
    else:
        return render(request, "login.html")


def logout_view(request):
    if request.method =="POST":
        logout(request)
        return render(request, "index.html", {"logout_message": "Logged out."})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            success = True
            return render(request, 'change_password.html', {"form": form, "success": success } )
        else:
            failure = True
            return render(request, 'change_password.html', {"form": form, "failure": failure})
    else:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        return render(request, "change_password.html", {"form": form})


# Function for handling all items when added to cart (different depending on type of item)
def item_handler(request):
    if request.method == "POST":
        # Retrieve all relevant item info to store in database
        user = request.user
        name = request.POST["name"]
        toppings_list = request.POST.getlist('toppings')
        type = request.POST["type"]
        # For Pizza, Sub, and Platter, size_price = "size;price"
        if (type != "Pasta") and (type != "Salad"):
            size_price = request.POST["size-price"]
        # For Pasta and Salad, there is only one size; as such, size_price = "price"
        else:
            size_price = request.POST["price"]
        # Format and save items to database/cart
        format_items(user, name, toppings_list, type, size_price)
        return redirect("/menu")
    else:
        return redirect("/menu")


# Function for removing items from user's cart
def remove_items(request):
    if request.method == "POST":
        # Delete item from database
        item_ID = request.POST['item-id']
        Item.objects.filter(id=item_ID).delete();

        return redirect('/orders')
