# Generated by Django 4.2.7 on 2023-11-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_siom', '0003_medicamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='quantidade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
