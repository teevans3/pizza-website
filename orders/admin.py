from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Pizza, Topping, Sub, SubTopping, Pasta, Salad, DinnerPlatter, Order, Item

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(SubTopping)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Item)


class OrderAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.CharField: {'widget': Textarea(attrs={'rows':10, 'cols':150})},
    }


admin.site.register(Order, OrderAdmin)
