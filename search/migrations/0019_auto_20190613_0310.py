# Generated by Django 2.1.7 on 2019-06-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0018_right'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='author',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sentence',
            name='eng_senetence',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sentence',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sentence',
            name='style',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentence',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]