# Generated by Django 2.1.3 on 2019-01-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('resume', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('image', models.FileField(upload_to='')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField()),
                ('last_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
