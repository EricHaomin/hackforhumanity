# Generated by Django 3.0.3 on 2020-02-23 00:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('user', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('resolved', models.BooleanField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]