from django.db import models


class Announcement(models.Model):
    game = models.CharField(max_length=200)
    place_name = models.CharField(max_length=200)
    place_location = models.CharField(max_length=200)
    place_lat = models.DecimalField(max_digits=9, decimal_places=6)
    place_long = models.DecimalField(max_digits=9, decimal_places=6)
    reader = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    game_type = models.CharField(max_length=200)
    metro = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200, null=True, blank=True)
