# Generated by Django 4.2.5 on 2023-11-05 22:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_cancha_id_cancha_alter_horariobase_id_bloque_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='id_cancha',
            field=models.UUIDField(default=uuid.UUID('b108bb42-e1c4-447a-9a84-cf024073b569'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='horariobase',
            name='id_bloque',
            field=models.UUIDField(default=uuid.UUID('a45850fa-3059-49c2-80bf-d9acdd61d816'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='horariocancha',
            name='id_horario',
            field=models.UUIDField(default=uuid.UUID('32d3cad4-da34-435b-b3ce-20c5cbcb5dd8'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='id_imagen',
            field=models.UUIDField(default=uuid.UUID('68486e1b-791b-4eb5-95da-4aa867767bee'), primary_key=True, serialize=False),
        ),
    ]