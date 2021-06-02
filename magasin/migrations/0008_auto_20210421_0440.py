# Generated by Django 3.2 on 2021-04-21 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0007_auto_20210421_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='adresse',
            field=models.TextField(default='null'),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
    ]
