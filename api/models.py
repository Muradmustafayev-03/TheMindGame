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


class Report(models.Model):
    REPORT_REASONS = [
        ('profile', 'Offensive nickname or profile photo'),
        ('inactivity', 'Inactivity during the game'),
        ('ruining', 'Intentional ruining the game'),
        ('cheating', 'Cheating')
    ]

    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING,
                             verbose_name='who has reported',
                             related_name='report_author',
                             )
    reported_user = models.ForeignKey(User,
                                      on_delete=models.CASCADE,
                                      verbose_name='who has been reported',
                                      related_name='reported_user'
                                      )
    reason = models.CharField(max_length=20, choices=REPORT_REASONS, default=REPORT_REASONS[0])
    description = models.CharField(max_length=300, blank=True, null=True)
    report_datetime = models.DateTimeField(auto_now=True)
