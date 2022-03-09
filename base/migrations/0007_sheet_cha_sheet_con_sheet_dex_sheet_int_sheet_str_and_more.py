# Generated by Django 4.0.2 on 2022-03-03 06:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0006_alter_sheet_classes_alter_sheet_lvl'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='cha',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30),
                                                              django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='sheet',
            name='con',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30),
                                                              django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='sheet',
            name='dex',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30),
                                                              django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='sheet',
            name='int',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30),
                                                              django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='sheet',
            name='str',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30),
                                                              django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='sheet',
            name='wis',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(30),
                                                              django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='alignment',
            field=models.CharField(choices=[('LG', 'Lawful Good'), ('NG', 'Neutral Good'), ('CG', 'Chaotic Good'),
                                            ('LN', 'Lawful Neutral'), ('TN', 'True Neutral'), ('CN', 'Chaotic Neutral'),
                                            ('LE', 'Lawful Evil'), ('NE', 'Neutral Evil'), ('CE', 'Chaotic Evil')],
                                   default='CG', max_length=2),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='lvl',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(20),
                                                             django.core.validators.MinValueValidator(1)]),
        ),
    ]