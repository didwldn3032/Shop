from django.urls import path
from .views import main, new, create, show , update, delete, comment, review, comment1, new2, show2, update2, delete2, main2, create2   

app_name = "posts" 
urlpatterns = [
    path('new/', new, name="new"),
    path('new2/', new2, name="new2"),
    path('comment1/', comment1, name="comment1"),
    path('review/', review, name="review"),
    path('create/', create, name="create"),
    path('create2/', create2, name="create2"),
    path('', main, name="main"),
    path('main2/', main2, name="main2"),
    path('show/<int:id>', show, name="show"),
    path('show2/<int:id>', show2, name="show2"),
    path('update/<int:post_id>/', update, name="update"),
    path('update2/<int:post_id>/', update2, name="update2"),
    path('delete/<int:id>/', delete, name="delete"),
    path('delete2/<int:id>/', delete2, name="delete2"),
    ]


