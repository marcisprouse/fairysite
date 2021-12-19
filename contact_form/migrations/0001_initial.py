# Generated by Django 3.2.5 on 2021-07-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]