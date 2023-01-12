from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    nickname = models.CharField(max_length=100)
    photo = models.ImageField(verbose_name='profile photo',
                              blank=True,
                              null=True)

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )

    # stats
    games_played = models.PositiveIntegerField(default=0)
    games_won = models.PositiveIntegerField(default=0)
    rounds_played = models.PositiveIntegerField(default=0)
    rounds_won = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname
