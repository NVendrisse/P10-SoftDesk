# Generated by Django 4.2.7 on 2024-01-25 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_rename_user_issue_author_issue_attributed_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
