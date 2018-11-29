from django.urls import path
# Same App importing
from food_providers.views import food_cook_info


urlpatterns = [

    path('food-cook-info/', food_cook_info, name='food-cook-info'),

]