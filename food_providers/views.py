from django.shortcuts import render
# Same App importing
from food_providers.models import CooKInfo


def food_cook_info(request):
    cook_info = CooKInfo.objects.all()
    template = 'food_providers/food_cook_info.html'
    context = {'cook_info': cook_info}
    return render(request, template, context)
