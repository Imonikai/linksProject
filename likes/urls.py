from django.urls import path

from likes.views import like_change

app_name = 'likes'

urlpatterns = [
    path('<int:link_pk>/', like_change, name='like_change'),
]