from django.urls import path
from .views import index, auth, like_comments
urlpatterns = [
    path('search_youtube/', index, name='index'),
    path('', auth, name='auth'),
    path('like_comment/', like_comments, name='like-comment')
]
