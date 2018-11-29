from django.urls import path
# Same App importing
from food_area.views import food_area_name


urlpatterns = [

    path('food-area-name/', food_area_name, name='food-area-name'),

]