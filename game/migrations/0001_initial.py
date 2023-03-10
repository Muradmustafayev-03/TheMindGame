# Generated by Django 4.1.5 on 2023-01-22 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.BooleanField(default=False)),
                ('players_number', models.PositiveIntegerField()),
                ('current_level', models.PositiveIntegerField()),
                ('levels', models.PositiveIntegerField()),
                ('card_on_table', models.PositiveIntegerField()),
                ('cards_remain', models.CharField(max_length=300)),
                ('lives', models.PositiveIntegerField()),
                ('throwing_stars', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
                ('room', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='game.room')),
            ],
        ),
    ]
