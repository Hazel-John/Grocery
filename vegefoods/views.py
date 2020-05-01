from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, OrderItem, Order, BillingInfo
from django.utils import timezone
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView, View
# Create your views here.
class IndexVView(ListView):
    model= Items
    template_name = "indexV.html"

class ProductSingleView(DetailView):
    model= Items
    template_name = "productsingle.html"

def checkout(request):
    return render(request, 'checkout.html')

def about(request):
    return render(request, 'about.html')

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
        context = {'orders': i.items.all()}
        #print(i.items.all())
        #for j in i.items.all():
         #   print (j)
    return render(request, 'cart.html', context)



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
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect("vegefoods:ordersummary")

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
            messages.info(request, "This item was not present in your cart.")
            return redirect("vegefoods:productsingle", slug=slug)
    else:
        messages.info(request, "You do not have an order yet!!!")
        return redirect("vegefoods:productsingle", slug=slug)


def indexV(request):
    return redirect('/')

def indexVsp(request,slug):
    return redirect('/')

class OrderSummaryView( LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'ordersummary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order!")
            return redirect('/')

def remove_single_item_from_cart(request, slug):
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
                #messages.info(request, "This item quantity was updated.")
            else:
                order_item.delete()

            return redirect("vegefoods:ordersummary")
        else:
            return redirect("vegefoods:ordersumamry")
    else:
        return redirect("vegefoods:ordersummary")

#class CheckoutView(View):
    #def get(self, *args, **kwargs):
     #   form = CheckoutForm()
      #  context = {
       #     'form': form
        #}
        #return render(self.request, "checkout.html", context)
    #def post(self, *args, **kwargs):
     #   form = CheckoutForm(self.request.POST or None)
      #  if form.is_valid():
      #      print("The form is valid")
       #     return redirect('vegefoods:checkout')

def checkout(request):
    if request.method == 'POST':
        name = request.POST['name']
        state = request.POST['state']
        street_address = request.POST["street_address"]
        apartment_address = request.POST["apartment_address"]
        city = request.POST["city"]
        zip = request.POST["zip"]
        phone = request.POST["phone"]
        #user_info = BillingInfo.objects.create(user=request.user)

        info_obj = BillingInfo(user=request.user, name=name, state=state, street_address=street_address,
                               apartment_address=apartment_address, city=city, zip=zip,
                               phone=phone)
        info_obj.save()
    return render(request, 'checkout.html')



def cartsp(request,slug):
    var= Order.objects.all().filter(user=request.user)
    print(type(var))
    for i in var:
        context = {'orders': i.items.all()}
    return render(request, 'cart.html', context)