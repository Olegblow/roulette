from django.db import models


class Artist(models.Model):
    """
    Хранит данные о артисте.
    """

    MAN = 1
    WOMAN = 2
    GENDER = (
        (MAN, 'Мужской'),
        (WOMAN, 'Женский')
    )

    full_name = models.CharField('Полное имя', max_length=127)
    nickname = models.CharField('Никнейм', max_length=127, blank=True)
    gender = models.PositiveIntegerField(
        'Гендер',
        choices=GENDER,
        default=WOMAN
    )
    birthday = models.DateField('День рождения')
    about = models.TextField('Об актере', blank=True)

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return self.full_name


class SocialNetwork(models.Model):
    """
    Хранит данные о соц сетях актеров.
    """

    OTHER = 1
    TWITTER = 2
    VK = 3
    TELEGRAM = 4
    INSTAGRAM = 5
    SOCIAL_NETWORKS_TYPE = (
        (OTHER, 'Другое'),
        (TWITTER, 'Твиттер'),
        (VK, 'Вк'),
        (TELEGRAM, 'Телеграмм'),
        (INSTAGRAM, 'Тнстаграм'),
    )

    artist = models.ForeignKey(
        Artist,
        verbose_name='артист',
        related_name='social_networks',
        on_delete=models.CASCADE
    )
    social_network_type = models.PositiveIntegerField(
        'соц. сеть',
        choices=SOCIAL_NETWORKS_TYPE,
        default=OTHER
    )
    name = models.CharField(max_length=127, blank=True)
    url = models.URLField(verbose_name='сслка', max_length=127)

    class Meta:
        verbose_name = 'Соц. сеть'
        verbose_name_plural = 'Соц. сети'

    def __str__(self):
        return self.url


class Movie(models.Model):
    """
    Хранит данные о кино.
    """

    name = models.CharField('Название', max_length=255)
    original_name = models.CharField(
        'Оригинальное название',
        max_length=255,
        blank=True
    )
    relise = models.DateField('Релиз')
    about = models.TextField('О кино', blank=True)
    artists = models.ManyToManyField(Artist, verbose_name='Артисты')
    url = models.URLField(
        verbose_name='сслка',
        max_length=255,
        blank=True
    )

    class Meta:
            verbose_name = 'Фильм'
            verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name
