"""point_mall_repeat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, path
from point_mall import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls.user_urls', namespace='oauth2_provider')),
    path('users/', include('user.urls.user_urls')),
    path('items/', include('item.urls.item_urls')),
    path('categories/', include('item.urls.category_urls')),
    path('me/', include('user.urls.me_urls')),
    path('media/uploads/item_images/<str:file_name>', views.image_view),
]
