from pydoc import describe

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from multiselectfield import MultiSelectField


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


"""
class Feature(models.Model):
    name = models.CharField(max_length=60, null=True)
    F_CHOICES = [
        ('Feature', 'Feature'),
        ('Trait', 'Trait'),
        ('Spell', 'Spell'),
    ]
    featureType = models.CharField(max_length=20, choices=F_CHOICES, default='Feature')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
"""
"""
class Equipment(models.Model):
    name = models.CharField(max_length=60, null=True)
    IS_WEAPON = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    classes = models.CharField(max_length=20, choices=IS_WEAPON, default='No')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
"""


class Sheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60, null=True)
    race = models.CharField(max_length=60, null=True)

    CLASS_CHOICES = [
        ('Fighter', 'Fighter'),
        ('Barbarian', 'Barbarian'),
        ('Rogue', 'Rogue'),
    ]
    classes = models.CharField(max_length=20, choices=CLASS_CHOICES, default='Fighter')

    lvl = models.IntegerField(default=1, validators=[MaxValueValidator(20), MinValueValidator(1)])
    exp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    background = models.CharField(max_length=60, null=True)
    inspiration = models.IntegerField(default=10, validators=[MinValueValidator(0)])

    armourAC = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    initiationRoll = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    maxHp = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    current = models.IntegerField(default=10)
    tempHp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    speed = models.IntegerField(default=30, validators=[MinValueValidator(0)])

    deathFail = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])
    deathSuccess = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])

    pp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    gp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    sp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cp = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    DICE_CHOICES = [
        ('d4', 'd4'),
        ('d6', 'd6'),
        ('d8', 'd8'),
        ('d10', 'd10'),
        ('d12', 'd12'),
    ]
    numHitDice = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    currentHitDice = models.IntegerField(default=0, validators=[MinValueValidator(0)]);
    hitDice = models.CharField(max_length=3, choices=DICE_CHOICES, default="d6")

    ALIGN_CHOICES = [
        ('LG', 'Lawful Good'),
        ('NG', 'Neutral Good'),
        ('CG', 'Chaotic Good'),
        ('LN', 'Lawful Neutral'),
        ('TN', 'True Neutral'),
        ('CN', 'Chaotic Neutral'),
        ('LE', 'Lawful Evil'),
        ('NE', 'Neutral Evil'),
        ('CE', 'Chaotic Evil'),
    ]
    alignment = models.CharField(max_length=2, choices=ALIGN_CHOICES, default='CG')

    str = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    dex = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    con = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    wis = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    int = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    cha = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])

    language = models.TextField(null=True, blank=True)
    proficiencies = models.TextField(null=True, blank=True)

    personality = models.TextField(null=True, blank=True)
    ideals = models.TextField(null=True, blank=True)
    bonds = models.TextField(null=True, blank=True)
    flaws = models.TextField(null=True, blank=True)

    SKILL_CHOICES = (('Acrobatics', 'Acrobatics (Dex)'),
                     ('Animal Handling', 'Animal Handling (Wis)'),
                     ('Arcana', 'Arcana (Int)'),
                     ('Athletics', 'Athletics (Str)'),
                     ('Deception', 'Deception (Cha)'),
                     ('History', 'History (Int)'),
                     ('Insight', 'Insight (Wis)'),
                     ('Intimidation', 'Intimidation (Cha)'),
                     ('Investigation', 'Investigation (Int)'),
                     ('Medicine', 'Medicine (Wis)'),
                     ('Nature', 'Nature (Wis)'),
                     ('Perception', 'Perception (Wis)'),
                     ('Performance', 'Performance (Cha)'),
                     ('Persuasion', 'Persuasion (Cha)'),
                     ('Religion', 'Religion (Int)'),
                     ('Sleight of Hand', 'Sleight of Hand (Dex)'),
                     ('Stealth', 'Stealth (Dex)'),
                     ('Survival', 'Survival (Wis)'),
                     )
    skills = MultiSelectField(choices=SKILL_CHOICES, default='Acrobatics')

    SAV_THROW = (('Str', 'Strength'),
                 ('Dex', 'Dexterity'),
                 ('Con', 'Constitution'),
                 ('Int', 'Intelligence'),
                 ('Wis', 'Wisdom'),
                 ('Cha', 'Charisma')
                 )
    savThrow = MultiSelectField(choices=SAV_THROW, blank=True, default='Str')

    notes = models.TextField(null=True, blank=True)

    # features = models.ManyToManyField(Feature)
    # equipments = models.ManyToManyField(Equipment)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
