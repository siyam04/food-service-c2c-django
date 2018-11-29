from django.urls import path
# Same App importing
from food_delivery.views import delivery_point


urlpatterns = [

    path('delivery-point/', delivery_point, name='delivery-point'),

]