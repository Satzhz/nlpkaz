# Generated by Django 2.1.7 on 2019-06-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0016_wordform_sentence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(default=0)),
                ('answer', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]