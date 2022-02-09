# Generated by Django 4.0.2 on 2022-02-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_sheet_lvl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='classes',
            field=models.CharField(choices=[('FIGHTER', 'Fighter'), ('WIZARD', 'Wizard'), ('CLERIC', 'Cleric')], default='Fighter', max_length=20),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='lvl',
            field=models.CharField(choices=[('Lvl. 1', '1'), ('Lvl. 2', '2'), ('Lvl. 3', '3')], default='1', max_length=7),
        ),
    ]
