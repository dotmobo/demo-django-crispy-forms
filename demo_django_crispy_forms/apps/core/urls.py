from django.conf.urls import patterns, url
from .views import RegistrationCreate, registration_success

urlpatterns = [
    url(r'^$', RegistrationCreate.as_view(), name='add'),
    url(r'^success/$', registration_success, name='success'),
]
