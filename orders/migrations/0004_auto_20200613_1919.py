# Generated by Django 3.0.2 on 2020-06-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_sub_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='all_items',
            field=models.CharField(max_length=10000),
        ),
    ]
