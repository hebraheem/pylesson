from django.urls import path

from watch_list.views import MovieList, MovieDetail

urlpatterns = [
    path('list/', MovieList, name="movie_list" ),
    path('<int:pk>',MovieDetail , name="movie_detail" ),
]