# Generated by Django 4.0.5 on 2022-07-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(default='', upload_to='images/')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
    ]
