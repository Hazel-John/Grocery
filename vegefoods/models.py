from django.contrib import messages
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User, auth


CATEGORY_CHOICES = (
    ('V', 'Vegetables'),
    ('F', 'Fruits'),
    ('D', 'Dry Fruits'),
    ('J', 'Juices')
)

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    discount_price=models.IntegerField(blank=True, null=True)
    offer = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    slug = models.SlugField()
    def _str_(self):
        return  self.name
    def get_absolute_url(self):
        return reverse("vegefoods:productsingle", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("vegefoods:add-to-cart", kwargs={'slug': self.slug})
    def get_remove_from_cart_url(self):
        return reverse("vegefoods:remove-from-cart", kwargs={'slug': self.slug})

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
