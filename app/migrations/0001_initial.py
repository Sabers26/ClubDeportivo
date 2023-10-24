# Generated by Django 4.2.3 on 2023-10-17 18:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id_cancha', models.UUIDField(default=uuid.UUID('fcf27ab2-7f2f-46eb-9d18-173fa9157fba'), primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=80)),
                ('habilitado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaUsuario',
            fields=[
                ('id_cuenta', models.UUIDField(default=uuid.UUID('a03cd990-7c5e-4444-b928-cc29e4482e26'), primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=24)),
                ('es_admin', models.BooleanField(default=False)),
                ('rut_usuario', models.CharField(max_length=10)),
                ('nombre_usuario', models.CharField(max_length=30)),
                ('tipo_socio', models.CharField(choices=[('Socio Colaborador', 'SocioColab'), ('Socio', 'Socio'), ('ADMIN', 'ADMIN')], default=('Socio', 'Socio'), max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HorarioBase',
            fields=[
                ('id_bloque', models.UUIDField(default=uuid.UUID('b2edda24-510e-468e-8749-61637dff805a'), primary_key=True, serialize=False)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HorarioCancha',
            fields=[
                ('id_horario', models.UUIDField(default=uuid.UUID('aa6f96c8-e394-45df-93bb-85f16d660312'), primary_key=True, serialize=False)),
                ('fecha_horario', models.DateField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('id_bloque', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.horariobase')),
                ('id_cancha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cancha')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id_imagen', models.UUIDField(default=uuid.UUID('0f6081a9-8999-4edc-a807-dfe6aedf0176'), primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateField()),
                ('horario_cancha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.horariocancha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cuentausuario')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_noticia', models.CharField(max_length=100)),
                ('sub_titulo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('fecha_noticia', models.DateField()),
                ('cuerpo', models.TextField()),
                ('imagen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.imagen')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cuentausuario')),
            ],
        ),
    ]
