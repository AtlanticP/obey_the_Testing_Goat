from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('list/<int:list_id>/', views.list_view, name = 'list'),
	path('list/new/', views.new_list, name = 'new_list'),
    path('', views.home_page, name = 'home'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
