from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from watch_list.models import WatchList, StreamPlatform, Review
from watch_list.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

# @api_view(["GET","POST"])
# def MovieList(request) :
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#
#         return  response.Response(serializer.data)
#
#     if request.method == "POST":
#         seriallizer = MovieSerializer(data = request.data)
#         if(seriallizer.is_valid()):
#             seriallizer.save()
#             return response.Response(seriallizer.data)
#         else:
#             return response.Response(seriallizer.errors)

# @api_view(["GET","PATCH","DELETE"])
# def MovieDetail(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return response.Response({"Error": "Movie not found "}, status=status.HTTP_404_NOT_FOUND)
#
#     if(request.method == "GET"):
#         serializer = MovieSerializer(movie)
#
#         return response.Response(serializer.data)
#
#     if (request.method == "PATCH"):
#         # movie = Movie.objects.get(pk=pk)
#         seriallizer = MovieSerializer(movie, data = request.data)
#         if seriallizer.is_valid():
#             seriallizer.save()
#             return response.Response(seriallizer.data)
#         else:
#             return response.Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         # movie= Movie.objects.get(pk=pk)
#         movie.delete()
#
#         return response.Response(status= status.HTTP_204_NO_CONTENT)

class MovieListAv(APIView):

    def get(self, request):
        movie = WatchList.objects.all()
        serializer = WatchListSerializer(movie, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return  response.Response({"Error": "Creation failed"}, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAv(APIView):
    def get(self,request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return response.Response({"Error": "item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return response.Response(serializer.data, status=status.HTTP_200_OK)



    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return response.Response({"Error": "item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return response.Response({"Error": "item not found"}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()

        return response.Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformView(APIView) :
    def get(self, request):
        streams  = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streams, many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatfromDetail(APIView):

    def get(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return response.Response({"Error": "stream not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(stream)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return response.Response({"Error": "stream not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(stream, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return response.Response({"Error": "stream not found"}, status=status.HTTP_404_NOT_FOUND)

        stream.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

class ReviewAv(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self, request,*args, **kwargs):
        return  self.create(request,*args, **kwargs)


class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

