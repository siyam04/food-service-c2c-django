from django.urls import path
# Same App importing
from food_items.views import food_categories, all_food_items, food_details, add_items, categorywise_food

urlpatterns = [

    path('categories/', food_categories, name='categories'),
    path('add-items/', add_items, name='add-items'),
    path('all-food-items/', all_food_items, name='all-food-items'),
    path('categorywise-items/<int:id>/', categorywise_food, name='categorywise-items'),
    path('food-details/<int:pk>/', food_details, name='food-details'),

]