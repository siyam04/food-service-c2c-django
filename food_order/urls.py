from django.urls import path
# Same App importing
from food_order.views import order_details_info, order_form, client_info


urlpatterns = [

    path('order-details/<int:id>/', order_details_info, name='order-details'),
    path('order-form/<int:id>/', order_form, name='order-form'),
    path('client-info/', client_info, name='client-info'),
]