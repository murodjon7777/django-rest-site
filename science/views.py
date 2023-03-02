from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
# Create your views here.
from .models import Person,Author
from .serializers import TodoSerializer,AuthorSerializer

class ListTodo(ListAPIView):
    queryset=Person.objects.all()
    serializer_class=TodoSerializer
    
class DetailTodo(RetrieveAPIView):
    queryset=Person.objects.all()
    serializer_class=TodoSerializer

class ListAuthor(ListAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
class DetailAuthor(RetrieveAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    

