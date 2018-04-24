from django.urls import path
from django.conf.urls import include, url
from lists import views as list_views
from lists import urls as lists_urls
from accounts import urls as accounts_urls

urlpatterns = [
	path('accounts/', include(accounts_urls)),
	path('list/', include(lists_urls)),
    path('', list_views.home_page, name = 'home'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)