# Generated by Django 4.2.5 on 2023-11-05 21:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customuser_is_superuser_alter_cancha_id_cancha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='id_cancha',
            field=models.UUIDField(default=uuid.UUID('7429168e-d5b8-4997-8b9f-8d627ccc4487'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='horariobase',
            name='id_bloque',
            field=models.UUIDField(default=uuid.UUID('f0fa50e3-864c-4016-aa69-cfcf423ac3b6'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='horariocancha',
            name='id_horario',
            field=models.UUIDField(default=uuid.UUID('e81dd6d5-0777-4c90-8d49-5e9f9fc0b6c1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='id_imagen',
            field=models.UUIDField(default=uuid.UUID('f6195b26-28e6-4239-a9d8-8e5c12f28e93'), primary_key=True, serialize=False),
        ),
    ]