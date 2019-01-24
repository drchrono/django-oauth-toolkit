# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("oauth2_provider", "0004_merge")]

    operations = [
        migrations.AlterIndexTogether(
            name="refreshtoken", index_together=set([("application_id", "user_id")])
        ),
    ]
