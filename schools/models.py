from django.db import models
from django.utils.text import slugify


class Municipal_Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Levels(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level


class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender


class Schools(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(null=True, blank=True)
    municipal_area = models.ForeignKey(
        Municipal_Area, on_delete=models.DO_NOTHING)
    level = models.ForeignKey(
        Levels, on_delete=models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey(
        Gender, on_delete=models.DO_NOTHING, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Create your models here.
