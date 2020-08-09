from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Post2
# Create your views here.

def new(request):
    return render(request,'posts/new.html')

def new2(request):
    return render(request,'posts/new2.html')    

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        content2 = request.POST.get('content2')
        content3 = request.POST.get('content3')
        image = request.FILES.get('image')
        Post.objects.create(title=title, content=content, content2=content2, content3=content3, image = image) 
        user = request.user
        return redirect('posts:main')

def create2(request):
    if request.method == "POST2":
        title = request.POST2.get('title')
        content = request.POST2.get('content')
        content2 = request.POST2.get('content2')
        content3 = request.POST2.get('content3')
        image = request.FILES.get('image')
        Post2.objects.create(title=title, content=content, content2=content2, content3=content3, image = image) 
        user = request.user
        return redirect('posts:main2')        

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})

def main2(request):
    posts2 = Post2.objects.all()
    return render(request, 'posts/main2.html', {'posts2': posts2})

def show(request, id):
    post = Post.objects.get(pk=id)
    post.view_count +=1
    post.save()
    return render(request, 'posts/show.html', {'post': post})

def show2(request, id):
    post2 = Post2.objects.get(pk=id)
    post2.view_count +=1
    post2.save()
    return render(request, 'posts/show2.html', {'post2': post2})


def update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.content = request.POST['content2']
        post.content = request.POST['content3']
        post.image = request.FILES.get('image')
        post.save()
        return redirect('posts:show', post.id)
    return render(request, 'posts/update.html', {"post":post})

def update2(request, id):
    post2 = get_object_or_404(Post2, pk=id)
    if request.method == "POST2":
        post2.title = request.POST2['title']
        post2.content = request.POST2['content']
        post2.content = request.POST2['content2']
        post2.content = request.POST2['content3']
        post2.image = request.FILES.get('image')
        post2.save()
        return redirect('posts:show2', post2.id)
    return render(request, 'posts/update2.html', {"post2":post2})    

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("posts:main")

def delete2(request, id):
    post2 = get_object_or_404(Post2, pk=id)
    post2.delete()
    return redirect("posts:main")

def comment(request):
    if request.method == "REVIEW":
        content = request.POST.get('content')
        content2 = request.POST.get('content2')
        REVIEW.objects.create(content=content, content2=content2, content3=content3) 
        user = request.user
        return redirect('posts:review')

def review(request):
    return render(request, 'posts/review.html')

def comment1(request):
    return render(request,'posts/comment1.html')
# Create your views here.
