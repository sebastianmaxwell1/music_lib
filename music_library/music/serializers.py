from rest_framework import serializers
from .models import Song


# class SongSerializer(serializers.ModelSerializer):
# class Meta:
#     model = Song
#     fields = ['id', 'title', 'artist', 'album', 'release_date']

class SongSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, max_length=50)
    artist = serializers.CharField(required=True, allow_blank=False, max_length=50)
    album = serializers.CharField(required=True, allow_blank=False, max_length=50)
    release_date = serializers.DateTimeField(allow_null=False)

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('artist', instance.album)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance
