from pydoc import describe
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Sheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60)
    LVL_CHOICES = [
        ('Lvl. 1', '1'),
        ('Lvl. 2', '2'),
        ('Lvl. 3', '3'),
    ]

    lvl = models.CharField(max_length=7, choices=LVL_CHOICES, default='1')

    CLASS_CHOICES = [
        ('FIGHTER', 'Fighter'),
        ('WIZARD', 'Wizard'),
        ('CLERIC', 'Cleric'),
    ]

    classes = models.CharField(max_length=20, choices=CLASS_CHOICES, default='Fighter')

    ALIGN_CHOICES = [
        ('LG', 'Lawful Good'),
        ('NG', 'Neutral Good'),
        ('CG', 'Chaotic Good'),
    ]
    alignment = models.CharField(max_length=2, choices = ALIGN_CHOICES, default='Chaotic Good')

    description = models.TextField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

"""
"""