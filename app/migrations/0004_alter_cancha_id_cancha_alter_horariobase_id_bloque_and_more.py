# Generated by Django 4.2.5 on 2023-11-05 21:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cancha_id_cancha_alter_horariobase_id_bloque_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='id_cancha',
            field=models.UUIDField(default=uuid.UUID('66972c65-e589-46c4-a8b8-c42a61048591'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='horariobase',
            name='id_bloque',
            field=models.UUIDField(default=uuid.UUID('10138fef-c852-4013-9775-7983075f5057'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='horariocancha',
            name='id_horario',
            field=models.UUIDField(default=uuid.UUID('3dc2d7e7-b636-464f-bef8-036c3afb65b8'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='id_imagen',
            field=models.UUIDField(default=uuid.UUID('94077152-546d-4cf3-b475-105af8574689'), primary_key=True, serialize=False),
        ),
    ]