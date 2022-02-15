from rest_framework import serializers

from watch_list.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer) :
    review = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
    # id = serializers.IntegerField(read_only=True)
    # name= serializers.CharField()
    # description = serializers.CharField()
    # published = serializers.BooleanField()
    #
    # def create(self, validated_data):
    #     return WatchList.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.published = validated_data.get("published", instance.published)
    #     instance.save()
    #     return instance

