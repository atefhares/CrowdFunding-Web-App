# Generated by Django 3.0.4 on 2020-04-02 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200331_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='/media/profile_pic/jo.jpg', upload_to='profile_pic'),
        ),
    ]