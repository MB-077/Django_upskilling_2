# Generated by Django 5.0.6 on 2024-06-29 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_comment_user_comment_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
    ]
