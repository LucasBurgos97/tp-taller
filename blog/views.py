from django.shortcuts import render
from .models import Post

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

def mostrar(request):
    return render(request,'blog/l.html')