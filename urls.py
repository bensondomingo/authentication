from django.urls import include, path, re_path
from allauth.account.views import ConfirmEmailView
from django.conf import settings

urlpatterns = [
    path('api/', include('authentication.api.urls')),
]

if not settings.AUTHENTICATION_API_ONLY:
    urlpatterns += [path('accounts/', include('allauth.account.urls')), ]