from django.urls import path
from .views import *
app_name = "posts" 
urlpatterns = [
    path('new/', create, name="create"),
    path('review/', review, name="review"),
    path('', main, name="main"),
    path('main2/', main2, name="main2"),
    path('show/<int:id>', show, name="show"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
    path('<int:comment_id>/update_comment/', update_comment, name="update_comment"),
    path('<int:comment_id>/delete_comment/', delete_comment, name="delete_comment"),
    path('<int:post_id>/post_like',post_like, name="post_like"),
    path('like_list/', like_list, name="like_list"),
    ]
