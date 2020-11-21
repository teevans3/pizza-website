from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topping(models.Model):
    topping = models.CharField(max_length = 50)

    def __str__(self):
        return self.topping


class Pizza(models.Model):
    type_choices = (
        ('Regular', 'Regular'),
        ('Sicilian', 'Sicilian'))
    name = models.CharField(max_length=100) # (cheese), 1, 2, or 3 topping, Special
    type = models.CharField(max_length=15, choices=type_choices)
    smallprice = models.DecimalField(max_digits=4, decimal_places=2)
    largeprice = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return f"Name: {self.name} --- Type: {self.type} --- Price (small): ${self.smallprice} --- Price (large): ${self.largeprice}"


class SubTopping(models.Model):
    topping = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return f"Topping: {self.topping} --- Price (toppings): {self.price}"


class Sub(models.Model):
    name = models.CharField(max_length=100)
    smallprice = models.DecimalField(max_digits=4, decimal_places=2)
    largeprice = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} --- Price (small): ${self.smallprice} --- Price (large): ${self.largeprice}"


class Pasta(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} --- Price: ${self.price}"


class Salad(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name} --- Price: ${self.price}"

class DinnerPlatter(models.Model):

    name = models.CharField(max_length=100)
    smallprice = models.DecimalField(max_digits=4, decimal_places=2)
    largeprice = models.DecimalField(max_digits=4, decimal_places=2)


    def __str__(self):
        return f"Name: {self.name}  --- Price (small): ${self.smallprice} --- Price (large): ${self.largeprice}"


class Order(models.Model):
    status_choices = (
        ("INCOMPLETE", "INCOMPLETE"), # "incomplete" only chosen if something is wrong with order or transaction
        ("PENDING", "PENDING"),
        ("COOKING", "COOKING"),
        ("QUALITY CHECK", "QUALITY CHECK"),
        ("DELIVERING", "DELIVERING"),
        ("COMPLETE", "COMPLETE"))

    number = models.IntegerField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    total_items = models.IntegerField() # Number of items
    total_price = models.DecimalField(max_digits=6, decimal_places=2) # Total price
    all_items = models.CharField(max_length=10000) # List of all items for particular order
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices, default="PENDING")

    def __str__(self):
        return f"Order Number: {self.number} --- User: {self.user} --- Total Items: {self.total_items} --- Total: {self.total_price} --- Time: {self.time} -- Status: {self.status}"


class Item(models.Model):
    status_choices = (
        ("IN CART", "IN CART"), # "In cart", thus not ordered yet
        ("IN ORDER", "IN ORDER")) # Currently being processed, cooked, delivered, etc. / Also used if item is complete.
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    size = models.CharField(max_length=10) # sm. or lrg. or NA
    name = models.CharField(max_length=100) # Cheese, 1 Topping, Ham + Cheese (sub), Antipasto, etc.
    type = models.CharField(max_length=100) # Reg. pizza, Sic. pizza, Sub, Pasta, Salad, Platter
    toppings = models.CharField(max_length=250) # none/NA, mushrooms, green peppers + pepperoni, etc.
    price = models.DecimalField(max_digits=4, decimal_places=2)
    order_number = models.IntegerField()
    order = models.ForeignKey(Order, related_name='items', blank=True, null=True, on_delete=models.CASCADE) # Each item belongs to a particular order
    status = models.CharField(max_length=20, choices=status_choices, default="IN CART")

    def __str__(self):
        return f"Item ID: {self.id} --- Order Number: {self.order_number} --- User: {self.user} --- Size: {self.size} --- Name: {self.name} --- Type: {self.type} --- Toppings: {self.toppings} --- Price: ${self.price} --- Status: {self.status}"
