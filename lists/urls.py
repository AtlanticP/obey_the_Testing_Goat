from django.urls import path
from . import views

urlpatterns = [
	path('list/<int:list_id>/add_item', views.add_item, name = 'add_item'),
	path('list/<int:list_id>/', views.list_view, name = 'list'),
	path('list/new/', views.new_list, name = 'new_list'),
    path('', views.home_page, name = 'home'),
]
