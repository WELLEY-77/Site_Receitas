# Generated by Django 4.1.6 on 2023-04-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False, verbose_name='Publicada'),
        ),
    ]
