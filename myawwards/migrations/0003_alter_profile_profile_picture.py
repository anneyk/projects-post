# Generated by Django 3.2.13 on 2022-06-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
