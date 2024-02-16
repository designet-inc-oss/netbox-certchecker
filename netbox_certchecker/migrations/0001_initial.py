# Generated by Django 4.2.8 on 2024-02-09 02:11

from django.db import migrations, models
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0185_gfk_indexes'),
        ('extras', '0105_customfield_min_max_values'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=254)),
                ('url', models.URLField(max_length=1024)),
                ('comments', models.TextField(blank=True)),
                ('cert', models.FileField(upload_to='certchecker/%Y/%m/%d/')),
                ('alert', models.BooleanField()),
                ('device', models.ManyToManyField(blank=True, to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]