# Generated by Django 4.1.2 on 2022-10-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nif', models.IntegerField()),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_1', models.CharField(max_length=20)),
                ('apellid_2', models.CharField(max_length=20)),
                ('codigo_departamento', models.IntegerField()),
            ],
        ),
    ]