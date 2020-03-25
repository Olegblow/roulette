from rest_framework import viewsets

from core.models import Movie
from core.serializers import MovieSerializer


class MovieList(viewsets.ModelViewSet):
    """Вьюха списка фильмов."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
