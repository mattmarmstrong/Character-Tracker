# Generated by Django 4.0.2 on 2022-02-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_sheet_alignment_sheet_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='lvl',
            field=models.CharField(choices=[('1', 'Lvl. 1'), ('2', 'Lvl. 2'), ('3', 'lvl. 3')], default='1', max_length=7),
        ),
    ]