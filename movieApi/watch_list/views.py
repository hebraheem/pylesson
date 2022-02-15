from django.shortcuts import render
from django.http import JsonResponse

from watch_list.models import Movie

# Create your views here.

def MovieList(respons):
    movies = Movie.objects.all()
    data = {"movies": list(movies.values())}

    return JsonResponse(data)

def MovieDetail(response, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        "name": movie.name,
        "description": movie.description,
        "published": movie.published
    }

    return JsonResponse(data)

