from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Same App importing
from food_items.models import FoodItems
from food_order.forms import OrderForm
from food_order.models import Order
# Same App importing
from food_order.models import Client
from food_area.models import Area
from food_delivery.models import DeliveryPoint
from food_providers.models import CooKInfo
from food_users_profile.models import Profile


def order_details_info(request, id):
    order_details = Order.objects.get(id=id)
    price = order_details.quantity * order_details.food_name.price
    template = 'food_order/order_details.html'
    context = {
        'order_details': order_details,
        'price': price
    }

    return render(request, template, context)


@login_required(login_url='signup')
def order_form(request, id=None, provider_id=None, deliver_id=None, area_id=None):
    if request.method == 'POST':
        order_form_info = OrderForm(request.POST)

        if order_form_info.is_valid():
            order = order_form_info.save(commit=False)
            if order.food_name.minimum_quantity > order.quantity:
                return HttpResponse("Please Select The Minimum Quantity")
            else:
                order.save()
                return redirect('order-details', id=order.id)

    else:
        food = FoodItems.objects.get(id=id)
        profile = Profile.objects.get(user=request.user)
        initial_data = {
            "client_info": profile,
            "quantity": food.minimum_quantity,
            "food_name": FoodItems.objects.get(id=id),
            "provider": CooKInfo.objects.get(id=provider_id),
            "delivery_point": DeliveryPoint.objects.get(id=deliver_id),
            "area": Area.objects.get(id=area_id)
        }
        order_form_info = OrderForm(initial=initial_data)

    return render(request, 'food_order/order_form.html', {'order_form_info': order_form_info})


def client_info(request):
    client_details = Client.objects.all()
    template = 'food_order/client_info.html'
    context = {'client_details': client_details}
    return render(request, template, context)
