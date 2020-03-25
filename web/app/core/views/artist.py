from rest_framework import viewsets

from core.models import Artist
from core.serializers import ArtistSerializer


class ArtistList(viewsets.ModelViewSet):
    """Вьюха списка артистов."""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
