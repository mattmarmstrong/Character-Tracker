from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from multiselectfield import MultiSelectField


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Feat(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    numberRatings = models.IntegerField(default=0)

    @property
    def avg_fun_rating(self):
        avg = self.feat_rating.all().aggregate(Avg('fun')).get('fun__avg', 0)
        if avg is None:
            return 0.0
        else:
            return round(avg, 1)

    @property
    def avg_useful_rating(self):
        avg = self.feat_rating.all().aggregate(Avg('usefulness')).get('usefulness__avg')
        if avg is None:
            return 0.0
        else:
            return round(avg, 1)

    @property
    def total_rating(self):
        total = self.feat_rating.all().annotate(rate_count=Count('fun'))
        if total is None:
            return 0.0
        else:
            return total

    def __str__(self):
        return self.name


class Rating(models.Model):
    RATING_CHOICES = [
        (1, '1 - Trash'),
        (2, '2 - Bad'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Amazing'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feat = models.ForeignKey(Feat, on_delete=models.CASCADE, related_name='feat_rating')

    fun = models.IntegerField(choices=RATING_CHOICES)
    usefulness = models.IntegerField(choices=RATING_CHOICES)

    comment = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return str(self.user)


class Sheet(models.Model):
    """
    The sheet model that users will use CRUD operations, fields are relevant to 5e DnD playable character
    """

    # header
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=60, null=True)
    lvl = models.IntegerField(default=1, validators=[MaxValueValidator(20), MinValueValidator(1)])
    race = models.CharField(max_length=60, null=True)

    CLASS_CHOICES = [
        ('Barbarian', 'Barbarian'),
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Druid', 'Druid'),
        ('Fighter', 'Fighter'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcerer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard')
    ]
    classes = models.CharField(max_length=20, choices=CLASS_CHOICES, default='Fighter')

    background = models.CharField(max_length=60, null=True)

    ALIGN_CHOICES = [
        ('Lawful Good', 'Lawful Good'),
        ('Neutral Good', 'Neutral Good'),
        ('Chaotic Good', 'Chaotic Good'),
        ('Lawful Neutral', 'Lawful Neutral'),
        ('True Neutral', 'True Neutral'),
        ('Chaotic Neutral', 'Chaotic Neutral'),
        ('Lawful Evil', 'Lawful Evil'),
        ('Neutral Evil', 'Neutral Evil'),
        ('Chaotic Evil', 'Chaotic Evil'),
    ]
    alignment = models.CharField(max_length=20, choices=ALIGN_CHOICES, default='Chaotic Good')
    exp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    inspiration = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    # statistics
    str = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    dex = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    con = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    wis = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    int = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])
    cha = models.IntegerField(default=10, validators=[MaxValueValidator(30), MinValueValidator(0)])

    # saving throws
    SAV_THROW = [('Str', 'Strength'),
                 ('Dex', 'Dexterity'),
                 ('Con', 'Constitution'),
                 ('Int', 'Intelligence'),
                 ('Wis', 'Wisdom'),
                 ('Cha', 'Charisma')
                 ]
    savThrow = MultiSelectField(choices=SAV_THROW, blank=True)

    # battle
    numHitDice = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    currentHitDice = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    DICE_CHOICES = [
        ('d4', 'd4'),
        ('d6', 'd6'),
        ('d8', 'd8'),
        ('d10', 'd10'),
        ('d12', 'd12'),
    ]
    hitDice = models.CharField(max_length=3, choices=DICE_CHOICES, default="d6")
    initiationRoll = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    speed = models.IntegerField(default=30, validators=[MinValueValidator(0)])
    maxHp = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    current = models.IntegerField(default=10)
    tempHp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    deathFail = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])
    deathSuccess = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])

    # equipment
    armourAC = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    pp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    gp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    sp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cp = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    equipment = models.TextField(null=True, blank=True)

    # skills
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
    skills = MultiSelectField(choices=SKILL_CHOICES, blank=True)

    # language and other proficiencies
    language = models.TextField(null=True, blank=True)
    proficiencies = models.TextField(null=True, blank=True)

    # personality
    personality = models.TextField(null=True, blank=True)
    ideals = models.TextField(null=True, blank=True)
    bonds = models.TextField(null=True, blank=True)
    flaws = models.TextField(null=True, blank=True)

    # other
    feats = models.ManyToManyField(Feat, blank=True)  # unused right now, not vital to any epic
    features = models.TextField(null=True, blank=True)
    spells = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
