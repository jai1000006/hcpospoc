# Generated by Django 2.1 on 2018-09-02 07:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posapp_be_users', '0003_auto_20180829_0904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, choices=[('PANASONIC', 'Panasonic'), ('SAMSUNG', 'Samsung'), ('ATUL', 'Atul'), ('NESTLE', 'Nestle'), ('ASTRALPIPES', 'Astral Pipes')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AUTOMOTIVE', 'Automotive'), ('BEAUTY', 'Beauty'), ('BOOKS', 'Books'), ('CELLPHONES', 'Cell Phones'), ('CONSUMER', 'Consumer'), ('GROCERY', 'Grocery'), ('SCIENTIFIC', 'Scientific'), ('INDUSTRIAL', 'Industrial')], default='CONSUMER', max_length=50),
        ),
    ]
