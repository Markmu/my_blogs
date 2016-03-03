# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Tag', null=True),
            preserve_default=True,
        ),
    ]
