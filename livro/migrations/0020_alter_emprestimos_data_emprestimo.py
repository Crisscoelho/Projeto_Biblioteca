# Generated by Django 4.2.4 on 2023-10-20 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0019_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(default=datetime.datetime(2023, 10, 20, 20, 17, 37, 74160)),
        ),
    ]
