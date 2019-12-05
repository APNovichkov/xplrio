# Generated by Django 2.2.7 on 2019-12-04 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xplrmain', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergopost',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='usergopost',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='usersavedpost',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='usersavedpost',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='uservisitedpost',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='uservisitedpost',
            name='user_id',
        ),
        migrations.AddField(
            model_name='usergopost',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='xplrmain.UserPost'),
        ),
        migrations.AddField(
            model_name='usergopost',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usersavedpost',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='xplrmain.UserPost'),
        ),
        migrations.AddField(
            model_name='usersavedpost',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='uservisitedpost',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='xplrmain.UserPost'),
        ),
        migrations.AddField(
            model_name='uservisitedpost',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]