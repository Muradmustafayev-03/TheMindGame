from django.contrib import admin
from .models import Player, Room


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['profile', 'room']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'players_number', 'started']


admin.site.register(Player, PlayerAdmin)
admin.site.register(Room, RoomAdmin)
