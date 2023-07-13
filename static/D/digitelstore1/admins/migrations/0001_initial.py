# Generated by Django 2.1 on 2023-06-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pcat', models.CharField(max_length=50)),
                ('pcost', models.CharField(max_length=50)),
                ('pquality', models.CharField(max_length=50)),
                ('pdec', models.CharField(max_length=50)),
                ('pimage', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
