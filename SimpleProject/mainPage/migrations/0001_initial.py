# Generated by Django 2.0.3 on 2018-03-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputName', models.CharField(max_length=200)),
                ('inputEmail', models.EmailField(max_length=254)),
                ('inputTel', models.IntegerField()),
                ('submitTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
