# Generated by Django 4.1.1 on 2022-10-28 02:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0014_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 27, 23, 21, 26, 205115)),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='livro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livro.livros'),
        ),
    ]
