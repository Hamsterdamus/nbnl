from django.db import models


# Create your models here.

# Tournament
# PlayerCard
# Match

class Tournament(models.Model):
    STATUS_CHOICES = (
        ('planned', 'Запланирован'),
        ('cancelled', 'Отменен'),
        ('progress', 'Текущий'),
        ('done', 'Завершен'),
    )
    TournamentId = models.AutoField(primary_key=True, unique=True)
    Slug = models.SlugField(unique=True)
    TournamentName = models.CharField(max_length=500, verbose_name='Название турнира')
    TournamentDate = models.DateTimeField(verbose_name='Дата и время проведения турнира')
    TournamentDescription = models.TextField(verbose_name='Описание турнира')
    TournamentStatus = models.CharField(max_length=12, choices=STATUS_CHOICES, default='planned')

    # TODO PlayersList = models.ForeignKey(RegisteredPlayers, verbose_name='Список игроков турнира')
    class Meta:
        ordering = ["TournamentDate"]

    def __str__(self):
        return self.TournamentId


class PlayerCard(models.Model):
    PlayerId = models.AutoField(primary_key=True, unique=True)
    Slug = models.SlugField(unique=True)
    PlayerFirstName = models.CharField(max_length=10, verbose_name='Имя игрока')
    PlayerLastName = models.CharField(max_length=20, verbose_name='Фамилия игрока')
    PlayerEmail = models.EmailField(unique=True, verbose_name='e-mail Имя игрока')
    PlayerPic = models.ImageField(verbose_name='Фото игрока')
    PlayerBirth = models.DateField(verbose_name='Дата рождения игрока')
    PlayerRating = models.PositiveIntegerField(verbose_name='Рейтинг игрока')

    class Meta:
        ordering = ["PlayerFirstName"]

    def __str__(self):
        return self.PlayerId
