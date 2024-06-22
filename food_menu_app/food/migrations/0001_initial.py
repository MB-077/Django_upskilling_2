# Generated by Django 5.0.6 on 2024-06-22 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_desc', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
                ('item_image', models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5PTsuRj6pjDdRDNqaC27k705rxveiomd99w&s', max_length=500)),
            ],
        ),
    ]