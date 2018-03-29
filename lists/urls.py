from django.urls import path
from . import views

urlpatterns = [
	path('list/<int:list_id>/', views.list_view, name = 'list_view'),
	path('list/new/', views.new_list, name = 'new_list'),
    path('', views.home_page, name = 'home'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)