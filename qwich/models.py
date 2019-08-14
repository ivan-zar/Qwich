from django.db import models


class Announcement(models.Model):
    game = models.CharField(max_length=200)
    place_name = models.CharField(max_length=200)
    place_location = models.CharField(max_length=200)
    reader = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    game_type = models.CharField(max_length=200)
    metro = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200, blank=True)
    place_coord_long = models.FloatField()
    place_coord_lat = models.FloatField()



