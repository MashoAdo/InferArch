from django.urls import path
from arch.views import contact

urlpatterns = [
    path('contact/', contact, name='contact'),
]