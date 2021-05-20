from django.shortcuts import render

# Create your views here.
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, BookSerializer, BookSerializer
from .models import Book, Book
from rest_framework import filters
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import *
from .serializers import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            books = books.filter(title__icontains=title)

        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        Book_data = JSONParser().parse(request)
        Book_serializer = BookSerializer(data=Book_data)
        if Book_serializer.is_valid():
            Book_serializer.save()
            return JsonResponse(Book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse({'message': '{} books were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        books = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'The Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Book_serializer = BookSerializer(Book)
        return JsonResponse(Book_serializer.data)

    elif request.method == 'PUT':
        Book_data = JSONParser().parse(request)
        Book_serializer = BookSerializer(Book, data=Book_data)
        if Book_serializer.is_valid():
            Book_serializer.save()
            return JsonResponse(Book_serializer.data)
        return JsonResponse(Book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Book.delete()
        return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def book_list_published(request):
    books = Book.objects.filter(published=True)

    if request.method == 'GET':
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def Book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            books = books.filter(title__icontains=title)

        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        Book_data = JSONParser().parse(request)
        Book_serializer = BookSerializer(data=Book_data)
        if Book_serializer.is_valid():
            Book_serializer.save()
            return JsonResponse(Book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Book.objects.all().delete()
        return JsonResponse({'message': '{} books were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        books = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'The Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Book_serializer = BookSerializer(Book)
        return JsonResponse(Book_serializer.data)

    elif request.method == 'PUT':
        Book_data = JSONParser().parse(request)
        Book_serializer = BookSerializer(Book, data=Book_data)
        if Book_serializer.is_valid():
            Book_serializer.save()
            return JsonResponse(Book_serializer.data)
        return JsonResponse(Book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Book.delete()
        return JsonResponse({'message': 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def book_list_published(request):
    books = Book.objects.filter(published=True)

    if request.method == 'GET':
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            authors = authors.filter(title__icontains=title)

        authors_serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(authors_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        Author_data = JSONParser().parse(request)
        Author_serializer = AuthorSerializer(data=Author_data)
        if Author_serializer.is_valid():
            Author_serializer.save()
            return JsonResponse(Author_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Author.objects.all().delete()
        return JsonResponse({'message': '{} authors were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return JsonResponse({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Author_serializer = AuthorSerializer(Author)
        return JsonResponse(Author_serializer.data)

    elif request.method == 'PUT':
        Author_data = JSONParser().parse(request)
        Author_serializer = AuthorSerializer(Author, data=Author_data)
        if Author_serializer.is_valid():
            Author_serializer.save()
            return JsonResponse(Author_serializer.data)
        return JsonResponse(Author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Author.delete()
        return JsonResponse({'message': 'Author was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def Author_list_published(request):
    authors = Author.objects.filter(published=True)

    if request.method == 'GET':
        authors_serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(authors_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def Author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            authors = authors.filter(title__icontains=title)

        authors_serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(authors_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        Author_data = JSONParser().parse(request)
        Author_serializer = AuthorSerializer(data=Author_data)
        if Author_serializer.is_valid():
            Author_serializer.save()
            return JsonResponse(Author_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(Author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Author.objects.all().delete()
        return JsonResponse({'message': '{} authors were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def Author_detail(request, pk):
    try:
        Author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return JsonResponse({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Author_serializer = AuthorSerializer(Author)
        return JsonResponse(Author_serializer.data)

    elif request.method == 'PUT':
        Author_data = JSONParser().parse(request)
        Author_serializer = AuthorSerializer(Author, data=Author_data)
        if Author_serializer.is_valid():
            Author_serializer.save()
            return JsonResponse(Author_serializer.data)
        return JsonResponse(Author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Author.delete()
        return JsonResponse({'message': 'Author was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def author_list_published(request):
    authors = Author.objects.filter(published=True)

    if request.method == 'GET':
        authors_serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(authors_serializer.data, safe=False)