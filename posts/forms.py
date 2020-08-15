from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    _type = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="게시글 종류",
        choices=Post.POST_TYPES,
        required=True
    )
    class Meta:
        model = Post
        fields = ['title', '_type', 'content', 'image', 'price', 'remaining', 'gender']
        labels = {
            'title': '제목', 
            'content': '내용',
            'image': '게시글 사진',
            'price' : '가격',
            'remaining' : '재고',
            'gender' : '성별',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'remaining': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'gender': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }