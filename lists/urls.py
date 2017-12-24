from django.urls import path
from . import views

urlpatterns = [
	path('lists/the-only-list-in-the-world/', views.list_view, name = 'list'),
	path('lists/new/', views.new_list, name = 'list'),
    path('', views.home_page, name = 'home'),
]
