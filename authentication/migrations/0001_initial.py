# Generated by Django 4.1.4 on 2022-12-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=150)),
                ('city', models.TextField(max_length=150)),
                ('pin_code', models.IntegerField()),
                ('password1', models.CharField(max_length=25)),
                ('password2', models.CharField(max_length=25)),
            ],
        ),
    ]
