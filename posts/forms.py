from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content', 
            'image', 
            'price', 
            'remaining',
        ]
        labels = {
            'title': ('제목'), 
            'content': ('내용'),
            'image': ('게시글 사진'),
            'price' : ('가격'),
            'remaining' : ('재고'),
        }
        help_texts = {
            'title': ('제목을 입력해주세요.'),
            'content': ('내용을 입력해주세요.'),
            'price': ('가격을 입력해주세요.'),
            'remaining': ('재고를 입력해주세요.'),
        }

    def save(self, **kwargs):
        post = super().save(commit=False)
        post.user = kwargs.get('user', None)
        post.save()
        return post