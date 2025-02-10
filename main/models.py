from django.core.validators import MinValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='clubs/')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    max_income = models.FloatField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    max_expend = models.FloatField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.FloatField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club_from = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="club_from")
    club_to = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="club_to")
    price = models.FloatField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    price_tft = models.FloatField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name}"


