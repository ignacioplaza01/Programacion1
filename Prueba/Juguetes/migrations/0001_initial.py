# Generated by Django 4.1.3 on 2022-11-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juguetes',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=20)),
                ('producto', models.CharField(max_length=20)),
                ('edad', models.CharField(max_length=10)),
                ('precio', models.CharField(max_length=20)),
                ('cantidad', models.CharField(max_length=5)),
            ],
        ),
    ]