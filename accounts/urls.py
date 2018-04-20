from django.urls import path
from accounts import views


urlpatterns = [
	# path('list/<int:list_id>/', list_views.list_view, name = 'list_view'),
	# path('list/new/', lists_views.new_list, name = 'new_list'),

	path('send_email/', views.send_login_email, name='send_login_email'),
]