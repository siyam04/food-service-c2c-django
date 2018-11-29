from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage
)
# food_items App importing
from food_items.models import FoodItems, FoodCategory


def home(request):
    queryset_list = FoodItems.objects.all()
    all_category = FoodCategory.objects.all()

    # Searching
    query = request.GET.get('q', None)
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query) |
            Q(status__icontains=query)
        ).distinct()  # distinct used for not the duplicate search

    # Paginator shows 10 contacts per page
    paginator = Paginator(queryset_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    template = 'home.html'
    context = {
        'all_food_items': queryset,
        'lists': queryset_list,
        'page_request_var': page_request_var,
        'page': page,
        'all_category': all_category
    }

    return render(request, template, context)
