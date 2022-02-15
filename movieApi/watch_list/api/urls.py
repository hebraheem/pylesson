from django.urls import path

from watch_list.api.views import MovieListAv, MovieDetailAv, StreamPlatformView, StreamPlatfromDetail, ReviewAv, ReviewDetail

urlpatterns = [
    path('list/', MovieListAv.as_view(), name="movie_list" ),
    path('<int:pk>', MovieDetailAv.as_view() , name="movie_detail" ),
    path('stream/', StreamPlatformView.as_view(), name="stream_list" ),
    path('stream/<int:pk>', StreamPlatfromDetail.as_view(), name="stream_detail" ),
    path("reviews/", ReviewAv.as_view(), name="review-list"),
    path("reviews/<int:pk>", ReviewDetail.as_view(), name="review-detail")
]