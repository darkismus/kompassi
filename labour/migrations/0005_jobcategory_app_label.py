# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0004_auto_20141115_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcategory',
            name='app_label',
            field=models.CharField(default=b'labour', max_length=63, blank=True),
            preserve_default=True,
        ),
    ]