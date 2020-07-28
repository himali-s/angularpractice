from django.shortcuts import render
from rest_framework import viewsets, request
from api.models import Book
from api.serializers import BookSerializer
from django.http import HttpResponse

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#we are overrriding the already provided django rest_framework method
def post(self, request, *args, **kwargs):
    cover = request.data['cover']
    title =  request.data['title']
    Book.object.create(title=title, cover = cover)
    return HttpResponse({'message': 'Book created'}, status = 200 )



