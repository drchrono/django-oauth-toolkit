# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0002_08_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='redirect_uri',
            field=models.CharField(max_length=512),
        ),
    ]
