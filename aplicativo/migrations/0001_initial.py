# Generated by Django 5.0.3 on 2024-04-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=30)),
                ('curso_aluno', models.CharField(max_length=30))
            ],
        ),
    ]
