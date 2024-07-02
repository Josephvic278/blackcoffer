from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Info(models.Model):
    end_year = models.IntegerField(null=True,
    validators=[MinValueValidator(1800), MaxValueValidator], default=None)
    intensity = models.IntegerField(null=True, default=None)
    sector = models.CharField(max_length=255,null=True, default=None)
    topic = models.CharField(max_length=255, null=True)
    insight = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    start_year = models.IntegerField(null=True,
    validators=[MinValueValidator(1800), MaxValueValidator])
    impact = models.CharField(max_length=255, null=True)
    added = models.DateTimeField(null=True, default=None)
    published = models.DateTimeField(null=True)
    country = models.CharField(max_length=255, null=True)
    relevance = models.CharField(max_length=255, null=True)
    pestle = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    likelihood = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.title