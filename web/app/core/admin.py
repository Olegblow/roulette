from django.contrib import admin

from .models import Artist
from .models import Movie
from .models import SocialNetwork


class SocialNetworkInline(admin.TabularInline):
    """Инлайн соц. сетей."""

    model = SocialNetwork
    extra = 0


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Админка артиста."""

    inlines = [SocialNetworkInline]


@admin.register(Movie)
class MoveAdmin(admin.ModelAdmin):
    """Админка фильм."""

    pass
