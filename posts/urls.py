from django.urls import path
from .views import *
app_name = "posts" 
urlpatterns = [
    path('new/', new, name="new"),
    path('review/', review, name="review"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('main2/', main2, name="main2"),
    path('show/<int:id>', show, name="show"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('<int:post_id>/create_comment', create_comment, name="create_comment"),
    path('<int:comment_id>/update_comment/', update_comment, name="update_comment"),
    ]


# 여기는 원래 update_comment에 post_id 이름으로 보내주고 있었는데, 솔직히 이거는 이름 어떻게 사용하든 상관은 없어
# 대신 views.py에서 인자로 받는 변수명이랑 동일하게 작성해야 됨.
# 막 쓰면 헷갈리니까 그냥 알기 쉽게 comment_id로 변경하고 보면 됨. ㅇㅋ? 다시 views.py로 ㄱ

