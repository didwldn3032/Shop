from django.shortcuts import render

def open(request):
    return render(request, 'shopping/open.html')

def food(request):
    return render(request, 'shopping/food.html')

def fashion(request):
    return render(request, 'shopping/fashion.html')

def beauty(request):
    return render(request, 'shopping/beauty.html')

# Create your views here.




