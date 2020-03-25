from rest_framework import serializers

from .models import Artist
from .models import Movie
from .models import SocialNetwork


class MoveSetSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Move для сериализатора Artist."""

    class Meta:
        model = Movie
        fields = ('name', 'original_name', 'about', 'relise')


class SocialNetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialNetwork
        fields = ('social_network_type', 'name' , 'url')

class ArtistSerializer(serializers.ModelSerializer):
    """Сериализатор модели Artist."""

    movie_set = MoveSetSerializer(many=True)
    social_networks = SocialNetworkSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'full_name', 'nickname', 'gender',
                  'birthday', 'about', 'movie_set', 'social_networks')

    def create(self, validated_data):
        movies = validated_data.pop('movie_set')
        artist = Artist.objects.create(**validated_data)
        for movie in movies:
            movie_create = Movie.objects.create(**movie)
            movie_create.artists.add(artist)
        return artist


class MovieSerializer(serializers.ModelSerializer):
    """Сериализатор модели Movie"""

    artists = ArtistSerializer(many=True,)

    class Meta:
        model = Movie
        fields = ('name', 'original_name', 'about', 'relise', 'artists')
        depth = 1
