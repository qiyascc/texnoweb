# Generated by Django 4.1.11 on 2023-09-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texnoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimage',
            name='position',
            field=models.PositiveSmallIntegerField(choices=[(1, 'İlk'), (2, 'İkinci'), (3, 'Üçüncü')], default=1, unique=True),
        ),
    ]
