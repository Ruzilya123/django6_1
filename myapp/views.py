from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Post
from .serializers import PostSerializerV2
from django.views import View


class PostListV3(generics.ListCreateAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostSerializerV2


class PostDetailV3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerV2


class PostListV3(View):
    def get(self, request):
        objects = Post.objects.all()
        return render(request, 'all.html', {'items': objects})

    def post(self, request):
        print(request.POST)
        title = request.POST['title']
        Post.objects.create(title=title)
        return self.get(request)


class PostDetailV3(View):
    def get(self, request, pk):
        model = Post.objects.get(pk=pk)
        return render(request, 'one.html', {'item': model})
    
    def post(self, request, pk):
        model = Post.objects.get(pk=pk)
        new_title = request.POST['title']
        model.title = new_title
        model.save()
        return self.get(request, pk)
        

def deletePost(request, pk):
    model = Post.objects.get(pk=pk)
    model.delete()
    return redirect('/crud/')
