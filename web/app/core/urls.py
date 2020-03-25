from django.urls import include
from django.urls import path
from rest_framework import routers

from core.views import ArtistList
from core.views import Index
from core.views import MovieList


router = routers.DefaultRouter()
router.register(r'artists', ArtistList)
router.register(r'movies', MovieList)


urlpatterns = [
    path('', include(router.urls)),
    path('test/', Index.as_view(), name='index')
]
