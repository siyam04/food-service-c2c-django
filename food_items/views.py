from django.shortcuts import render, redirect
# Same App importing
from food_items.models import FoodItems, FoodCategory
from food_items.forms import FoodItemsForm


def food_categories(request):
    categories = FoodCategory.objects.all()
    template = 'food_items/food_categories.html'
    context = {'categories': categories}

    return render(request, template, context)

def categorywise_food(request, id):
    all_items = FoodItems.objects.filter(category__id=id)
    context = {'all_food_items': all_items}
    template = 'food_items/all_food_items.html'
    return render(request, template, context)


def all_food_items(request):
    all_items = FoodItems.objects.all()
    template = 'food_items/all_food_items.html'
    context = {'all_food_items': all_items}

    return render(request, template, context)


def food_details(request, pk):
    food_details_info = FoodItems.objects.get(id=pk)
    template = 'food_items/food_details.html'
    context = {'food_details_info': food_details_info}

    return render(request, template, context)


def add_items(request):
    if request.method == 'POST':
        add_items_info = FoodItemsForm(request.POST, request.FILES)
        if add_items_info.is_valid():
            obj = add_items_info.save()
            return food_details(request, obj.pk)

    else:
        add_items_info = FoodItemsForm()

    return render(request, 'food_items/add_items.html', {'add_items_info': add_items_info})
