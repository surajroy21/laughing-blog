from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog, Author
from .serializers import BlogListAPISerializer, AuthorListAPISerializer

# Create your views here.
class BlogListAPI(APIView):
    def get(self,request):
        blogs = Blog.objects.all()
        data = BlogListAPISerializer(blogs,many=True).data
        response = {
            "data": data,
            "success": True,
            "error": False
        }
        return Response(response, status=status.HTTP_200_OK)


class BlogDetailAPI(APIView):
    def get(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
            data = BlogListAPISerializer(blog).data
        except Blog.DoesNotExist:
            data = "No data found"
        response = {
            "data": data,
            "success": True,
            "error": False
        }
        return Response(response, status=status.HTTP_200_OK)


class BlogCreateAPI(APIView):
    def post(self,request):
        print('DATA: ',request.data)
        data=request.data
        blog = Blog.objects.create(
            title=data.get("title"),
            sub_title=data.get("sub_title"),
            author=data.get("author"),
            content=data.get("content"),
            description=data.get("description")
        )
        data = BlogListAPISerializer(blog).data
        response={
            "data":data,
            "success":True,
            "error":False
        }
        return Response(response, status=status.HTTP_200_OK)
        

class AuthorListAPI(APIView):
    def get(self,request):
        authors = Author.objects.all()
        data = AuthorListAPISerializer(authors, many=True).data

        response = {
            "data": data,
            "success":True,
            "error":False
        }
        return Response(response,status=status.HTTP_200_OK)


class AuthorDetailAPI(APIView):
    def get(self,request,id):
        try:
            author = Author.objects.get(id=id)
            data = AuthorListAPISerializer(author).data

        except Author.DoesNotExist:
            data="No Data found"

        response = {
            "data":data,
            "success":True,
            "error":False
        }
        return Response(response,status=status.HTTP_200_OK)

    class AuthorCreateAPI(APIView):
        def post(self,request):
            data = request.data
            author = Author.object.create(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                email=data.get("email"),
                mobile=data.get("mobile")
            )
            data = AuthorListAPISerializer(author).data
            response = {
                "data":data,
                "success":True,
                "error":False
            }
            return Response(response, status=status.HTTP_200_OK)

        