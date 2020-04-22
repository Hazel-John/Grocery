from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, OrderItem, Order
from django.utils import timezone
from django.views.generic import ListView, DetailView


# Create your views here.
class IndexVView(ListView):
    model= Items
    template_name = "indexV.html"

class ProductSingleView(DetailView):
    model= Items
    template_name = "productsingle.html"



def cart(request):
    print("Hello World")
   # context ={
    #    'orders': Order.objects.all().filter(user=request.user)
    #}
    #for i in context:
     #   print(i..items)
    var= Order.objects.all().filter(user=request.user)
    print(type(var))
    for i in var:
        print(i.items.all())
        for j in i.items.all():
            print (j)
    return render(request, 'cart.html')



def add_to_cart(request,slug):
    item = get_object_or_404(Items, slug=slug)
    # created-it's returning a tuple here
    order_item ,created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            #ordered_date = timezone.now()
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            #ordered_date = timezone.now()

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")

    return redirect("vegefoods:productsingle", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Items, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1

                order_item.save()
                messages.info(request, "This item quantity was updated.")
            else:
                order_item.delete()
                messages.info(request, "This item was removed from your cart.")
            return redirect("vegefoods:productsingle", slug=slug)
        else:
            # add a msg saying the order does not contain the item
            messages.info(request, "This item was not present in your cart.")
            return redirect("vegefoods:productsingle", slug=slug)
    else:
        # add a msg saying that the user does not have a order
        messages.info(request, "You do not have an order yet!!!")
        return redirect("vegefoods:productsingle", slug=slug)





