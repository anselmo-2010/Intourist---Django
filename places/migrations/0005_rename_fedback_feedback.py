# Generated by Django 3.2.5 on 2021-07-18 06:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0004_fedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fedback',
            new_name='Feedback',
        ),
    ]
