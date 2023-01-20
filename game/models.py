from django.db import models
from api.models import Profile


class Room(models.Model):
    players_number = models.PositiveIntegerField()

    current_level = models.PositiveIntegerField()
    levels = models.PositiveIntegerField()

    card_on_table = models.PositiveIntegerField()
    cards_remain = models.CharField(max_length=300)

    lives = models.PositiveIntegerField()
    throwing_stars = models.PositiveIntegerField()


class Player(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
