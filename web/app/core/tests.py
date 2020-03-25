# from django.test import TestCase

import pytest
from core.models import Artist, Movie


@pytest.mark.django_db
class TestModels:

    def test_artists(self):
        artist = Artist.objects.create(
            full_name='Ли СонГюн',
            nickname='nickname1',
            gender=1,
            birthday='1998-10-10',
            about='about about about test'
        )
        assert artist.full_name == 'Ли СонГюн'
        assert artist.gender == 1
        assert artist.birthday == '1998-10-10'
        assert 'about test' in artist.about
        assert str(artist) == artist.full_name

    def test_movie(self):
        movie = Movie.objects.create(
            name='тест кино',
            relise='2020-01-11',
            about='о тестлвом кино',
        )
        assert movie.about == 'о тестлвом кино'
        assert movie.name == 'тест кино'
        assert movie.relise == '2020-01-11'
        assert str(movie) == movie.name
