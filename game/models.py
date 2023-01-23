from django.db import models
from api.models import Profile
from .cards import *


class Room(models.Model):
    name = models.CharField(max_length=100)
    started = models.BooleanField(default=False)

    players_number = models.PositiveIntegerField(default=2)

    current_level = models.PositiveIntegerField(default=1)
    levels = models.PositiveIntegerField(default=10)

    card_on_table = models.PositiveIntegerField(default=0)
    cards_remain = models.CharField(max_length=300, default=new_deck())

    lives = models.PositiveIntegerField(default=2)
    throwing_stars = models.PositiveIntegerField(default=0)


class Player(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, default=None, null=True)
    cards = models.CharField(max_length=300, default='')
