"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path

from rango import views
from rango.views import AboutView, AddCategory, ProfileView

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('goto/', views.goto_url, name='goto'),
    path('search/', views.search, name='search'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('like/', views.like_category, name='like_category'),
    path('suggest/', views.suggest_category, name='suggest_category'),
    path('add/', views.auto_add_page, name='auto_add_page'),
]
