# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-01 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=63),
        ),
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, choices=[('MD', 'Maryland'), ('SD', 'South Dakota'), ('WY', 'Wyoming'), ('AS', 'American Samoa'), ('PR', 'Puerto Rico'), ('TN', 'Tennessee'), ('IA', 'Iowa'), ('GU', 'Guam'), ('IL', 'Illinois'), ('NC', 'North Carolina'), ('FL', 'Florida'), ('RI', 'Rhode Island'), ('NY', 'New York'), ('NJ', 'New Jersey'), ('VT', 'Vermont'), ('WI', 'Wisconsin'), ('VI', 'Virgin Islands'), ('IN', 'Indiana'), ('NE', 'Nebraska'), ('CO', 'Colorado'), ('DE', 'Delaware'), ('OR', 'Oregon'), ('MN', 'Minnesota'), ('MI', 'Michigan'), ('MA', 'Massachusetts'), ('MP', 'Northern Mariana Islands'), ('NH', 'New Hampshire'), ('ID', 'Idaho'), ('NM', 'New Mexico'), ('PA', 'Pennsylvania'), ('AZ', 'Arizona'), ('AK', 'Alaska'), ('MT', 'Montana'), ('KY', 'Kentucky'), ('GA', 'Georgia'), ('DC', 'District of Columbia'), ('SC', 'South Carolina'), ('LA', 'Louisiana'), ('OH', 'Ohio'), ('NA', 'National'), ('NV', 'Nevada'), ('MO', 'Missouri'), ('ND', 'North Dakota'), ('MS', 'Mississippi'), ('WA', 'Washington'), ('AR', 'Arkansas'), ('HI', 'Hawaii'), ('CT', 'Connecticut'), ('CA', 'California'), ('ME', 'Maine'), ('WV', 'West Virginia'), ('AL', 'Alabama'), ('KS', 'Kansas'), ('VA', 'Virginia'), ('OK', 'Oklahoma'), ('TX', 'Texas'), ('UT', 'Utah')], max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
