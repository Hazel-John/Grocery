from django.urls import path

from . import views
from .views import  (
    IndexVView,
    ProductSingleView,
    add_to_cart,
    remove_from_cart,
)

app_name = 'vegefoods'

urlpatterns = [
    path('', IndexVView.as_view(), name="indexV"),
    path('product-single/<slug>/', ProductSingleView.as_view(), name="productsingle"),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart"),
    path('cart', views.cart, name="cart"),
]
