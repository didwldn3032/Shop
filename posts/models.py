  
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name="상품명")
    content = models.TextField(verbose_name="상세보기")
    price = models.TextField(null = True, verbose_name="가격")
    remaining = models.TextField(null = True, verbose_name="재고")
    view_count = models.IntegerField(default = 0, verbose_name="조회수")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name="생성시간")
    updated_at = models.DateTimeField(auto_now = True, verbose_name="수정시간")
    image = models.ImageField(upload_to = 'images/', null = True, verbose_name="상품사진", blank="true")
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)


    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')

    @property
    def like_count(self):
        return self.like_user_set.count()
        
class Comment(models.Model): 
    content = models.TextField() 
    writer = models.ForeignKey(User, on_delete = models.CASCADE) 
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now = True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = (('user','post'))
# Create your models here.