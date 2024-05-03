# Generated by Django 5.0.4 on 2024-05-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='password',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='registration',
            name='password2',
            field=models.CharField(default='', max_length=15, verbose_name='Подтвердите пароль'),
        ),
    ]