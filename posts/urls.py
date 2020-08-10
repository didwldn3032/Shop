from django.urls import path
from .views import main, new, create, show , update, delete, comment, review, comment1, main2, create2  

app_name = "posts" 
urlpatterns = [
    path('new/', new, name="new"),
    path('comment1/', comment1, name="comment1"),
    path('review/', review, name="review"),
    path('create/', create, name="create"),
    path('create2/', create, name="create2"),
    path('', main, name="main"),
    path('main2/', main2, name="main2"),
    path('show/<int:id>', show, name="show"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    ]


