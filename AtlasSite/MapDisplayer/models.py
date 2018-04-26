from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.


class Map(models.Model):
    parentMap = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    width = models.IntegerField()
    height = models.IntegerField()
    imageURL = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='ni')
    summary = models.CharField(max_length=500, default='')
    full_link = models.CharField(max_length=100, default='')
    indices = ArrayField(models.IntegerField(default=0), default=list)
    isPrivate = models.BooleanField(default=False)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='Owned_Maps')
    viewers = models.ManyToManyField(User, blank=True, related_name='Accesible_Maps')

    def __str__(self):
        return self.name


class Region(models.Model):
    summary_link = models.CharField(max_length=100)
    full_link = models.CharField(max_length=100)
    indices = ArrayField(models.IntegerField())
    map_im_in = models.ForeignKey(
        Map,
        on_delete=models.CASCADE,)
    name = models.CharField(max_length=100, default='ni')

    def __str__(self):
        return self.name

