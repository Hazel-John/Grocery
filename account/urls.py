from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('checkout', views.checkout, name="checkout"),
    path('indexV', views.indexV, name="indexV"),
    path('about', views.about, name="about"),
   # path('productsingle', views.productsingle, name="productsingle"),


]