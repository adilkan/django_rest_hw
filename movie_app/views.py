from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie,Director,Review
from .serializer import SerializerReview,SerializerMovie,SerializerDirektor


@api_view(['GET'])
def director_list(request):
    director = Director.objects.all()
    serializer = SerializerDirektor(director,many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director(request,id):
    try:
        director = Director.objects.get(id=id)
    except:
        return Response(status=404)
    serializer = SerializerDirektor(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list(request):
    movie = Movie.objects.all()
    serializer = SerializerMovie(movie,many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        return Response(status=404)
    serializer = SerializerMovie(movie)
    return Response(data=serializer.data)

@api_view(["GET"])
def review_list(request):
    review = Review.objects.all()
    serializer = SerializerReview(review,many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review(request,id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=404)
    serializer = SerializerReview(review)
    return Response(data=serializer.data)
