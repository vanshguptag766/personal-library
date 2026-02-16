"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from record import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('addbook/', views.addbook, name='addbook'),
    path('delbook/', views.delbook, name='delbook'),
    path('delbook/<int:id>/', views.delbook, name='delbook_id'),
    path('viewbooks/', views.viewbooks, name='viewbooks'),
    path('updatebooks/', views.updatebook, name='updatebooks'),
    path('updatebook/<int:id>/', views.updatebook, name='updatebook_id'),
]
