# Generated by Django 3.2.5 on 2021-07-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(default=' ', max_length=500)),
                ('content', models.TextField(default=' ')),
            ],
        ),
    ]