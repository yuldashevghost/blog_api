from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Blog
from api.serializer import BlogSerializer


from django.http import JsonResponse

# def blog_list(request):
#     blogs = [
#         {"title": "Blog 1", "author": "Author 1", "category": "Category 1"},
#         {"title": "Blog 2", "author": "Author 2", "category": "Category 2"}
#     ]
#     return JsonResponse(blogs, safe=False)


# Create your views here.
@api_view(['GET'])
def home(request):
    api_url = {
        "List": "/blog-list/",
        "Create": "/blog-create/",
        "Update": "/blog-update/<str:pk>",
        "Delete": "/blog-delete/<str:pk>",
        "Detail": "/blog-details/<str:pk>",
    }
    return Response(api_url)

@api_view(['GET'])
def blog_list(request):
    model = Blog.objects.all()
    serializer = BlogSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_details(request, pk):
    model = Blog.objects.get(id=pk)
    serializer = BlogSerializer(model, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def blog_create(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def blog_update(request, pk):
    model = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=model, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def blog_delete(request, pk):
    model = Blog.objects.get(id=pk)
    model.delete()
    return Response("Blog deleted")