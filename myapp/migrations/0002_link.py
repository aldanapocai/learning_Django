# Generated by Django 3.1.4 on 2022-08-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.CharField(max_length=1000)),
                ('uuid', models.CharField(max_length=1000)),
            ],
        ),
    ]
