from django.urls import path

from . import views
from .views import  (
    IndexVView,
    ProductSingleView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
)

app_name = 'vegefoods'

urlpatterns = [
    path('', IndexVView.as_view(), name="indexV"),
    path('product-single/<slug>/', ProductSingleView.as_view(), name="productsingle"),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart"),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name="remove-single-item-from-cart"),
    path('ordersummary/', OrderSummaryView.as_view() , name="ordersummary"),
    path('ordersummary/indexV', views.indexV, name="indexV"),
    path('ordersummary/checkout', views.checkout, name="checkout"),
    path('ordersummary/ordersummary', OrderSummaryView.as_view() , name="ordersummary"),
    path('indexV', views.indexV, name="indexV"),
    path('checkout/', views.checkout, name="checkout"),
    path('product-single/<slug>/indexV', views.indexVsp, name="indexV"),
    path('product-single/<slug>/ordersummary', OrderSummaryView.as_view() , name="ordersummary"),
    #path('product-single/<slug>/checkout', views.checkout, name="ordersummary"),
]
