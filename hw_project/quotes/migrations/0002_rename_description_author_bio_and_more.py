# Generated by Django 4.2 on 2023-05-03 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='description',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='born_date',
            new_name='date_born',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='born_location',
            new_name='location_born',
        ),
    ]
