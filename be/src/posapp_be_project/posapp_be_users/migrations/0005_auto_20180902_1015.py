# Generated by Django 2.1 on 2018-09-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posapp_be_users', '0004_auto_20180902_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]