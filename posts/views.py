from django.shortcuts import render, redirect, redirect, get_object_or_404 
from .models import Post, Comment
import pdb
# Create your views here.

def new(request):
    return render(request,'posts/new.html')

def create(request):
    if request.method == "POST":
            title = request.POST.get('title',)
            content = request.POST.get('content')
            price = request.POST.get('price')
            remaining = request.POST.get('remaining')
            image = request.FILES.get('image')
            _type = request.POST.get('_type')
            user = request.user
            Post.objects.create(title=title, content=content, price=price, remaining=remaining, image = image, gender=gender, user=user, _type=_type) 
            return redirect('posts:main')
            

    

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})

def main2(request):
    posts = Post.objects.all()
    return render(request, 'posts/main2.html', {'posts': posts})

def show(request, id):    
    post = Post.objects.get(pk=id)
    post.view_count += 1
    post.save()  
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'posts/show.html', {'post': post, 'comments': all_comments})


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.price = request.POST['price']
        post.remaining = request.POST['remaining']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/update.html', {'post':post})

    



def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("posts:main")


def review(request):
    return render(request, 'posts/review.html')



def create_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404 (Post, pk=post_id)
        current_user = request.user
        comment_content = request.POST.get('content')
        Comment.objects.create(content=comment_content, writer=current_user, post=post)
    return redirect ('posts:show', post.pk)

# Create your views here.
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        comment.content = request.POST['content']
        comment.save()
        return redirect('posts:show', comment.post.id)
    return render(request, 'posts/update_comment.html', {'comment': comment}) # 여기서 comment를 읽을 수가 없음
    

    #아까 에러난 이유가 이렇게 post의 id 가 아니라 comment의 id로 넘겨줘서 인데,  models.py에서 Comment 모델 짠 걸 보면 알겠지만 comment에서 post의 정보를 가져올 수 있음
    # 그래서 comment.post.id 를 이용하면 comment를 작성한 post의 id 값을 가져올 수 있음.
    #  id 외에도 comment.post.title, comment.post.content 등등 가져올 수 있음
    # 그래서 comment를 우선 바깥으로 빼줌.
    # 그리고 show.html 이랑 urls.py를 보면 저기 여기부분이 urls.py에서 작성한 거랑 같은 변수로 사용하면 되는 부분임
    # 여기까지 하고 에러가 계속 나서 한동안 못 찾았었는데, 그 이유가 update_comment.html 파일에 보면

    #이거 보임?
    #기존 코드가 원래 이렇게 되어있었는데, 이러면 
    #넹
    