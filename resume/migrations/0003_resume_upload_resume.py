# Generated by Django 5.0.1 on 2024-04-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='upload_resume',
            field=models.FileField(blank=True, null=True, upload_to='resume'),
        ),
    ]
