# Generated by Django 3.0.4 on 2020-04-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegefoods', '0005_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]