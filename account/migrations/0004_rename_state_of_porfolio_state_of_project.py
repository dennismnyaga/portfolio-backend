# Generated by Django 5.1.1 on 2024-09-18 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_porfolio_git_repo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='porfolio',
            old_name='state_of',
            new_name='state_of_project',
        ),
    ]
