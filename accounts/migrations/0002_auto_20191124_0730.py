# Generated by Django 2.2.7 on 2019-11-24 07:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photography_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='risk_level',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
