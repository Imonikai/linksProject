from django.urls import path

from links.views import link_new

urlpatterns = [
    path('new/', link_new, name='link_new'),
]