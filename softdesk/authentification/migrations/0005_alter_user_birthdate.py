# Generated by Django 4.2.7 on 2023-12-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0004_alter_user_can_be_contacted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.IntegerField(default=0),
        ),
    ]