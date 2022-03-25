from django.forms import ModelForm
from .models import Sheet, Rating, Feat
from django import forms


class SheetForm(ModelForm):
    class Meta:
        model = Sheet
        fields = ['name',
                  'lvl',
                  'exp',
                  'race',
                  'background',
                  'classes',
                  'inspiration',
                  'armourAC',
                  'initiationRoll',
                  'maxHp',
                  'current',
                  'tempHp',
                  'speed',
                  'deathFail',
                  'deathSuccess',
                  'pp',
                  'gp',
                  'sp',
                  'cp',
                  'numHitDice',
                  'currentHitDice',
                  'hitDice',
                  'alignment',
                  'str',
                  'dex',
                  'con',
                  'wis',
                  'int',
                  'cha',
                  'language',
                  'proficiencies',
                  'personality',
                  'ideals',
                  'bonds',
                  'flaws',
                  'skills',
                  'savThrow',
                  # 'feats',
                  'features',
                  'equipment',
                  'spells',
                  'notes'
                  ]


class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['fun',
                  'usefulness',
                  # 'comment'
                  ]
