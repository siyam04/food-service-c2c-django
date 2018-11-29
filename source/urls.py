"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# Source Home importing
from source.views import home

# All Custom Apps Name
app_name = (

    'food_area',
    'food_order',
    'food_items',
    # 'food_clients',
    'food_delivery',
    'food_providers',
    'food_newsletters',
    'food_users_profile',

)

urlpatterns = [
    # Default ADMIN URL
    path('admin/', admin.site.urls),

    # Home URL
    path('home/', home, name='home'),

    # App URLS
    path('home/', include('food_area.urls')),
    path('home/', include('food_order.urls')),
    path('home/', include('food_items.urls')),
    # path('home/', include('food_clients.urls')),
    path('home/', include('food_delivery.urls')),
    path('home/', include('food_providers.urls')),
    path('home/', include('food_users_profile.urls')),

    # Food Category
    path('home/', include('food_items.urls')),

    # Newsletter App's URL
    path('newsletter/', include('food_newsletters.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
