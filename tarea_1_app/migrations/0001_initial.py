# Generated by Django 4.2.2 on 2023-06-22 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisprudencia',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('tipoCausa', models.CharField()),
                ('rol', models.CharField()),
                ('caratula', models.CharField()),
                ('nombreProyecto', models.CharField()),
                ('fechaSentencia', models.DateField()),
                ('descriptores', models.CharField()),
                ('linkSentencia', models.CharField()),
                ('urlSentencia', models.CharField()),
                ('activo', models.BooleanField()),
                ('tribunal', models.CharField()),
                ('tipo', models.CharField()),
                ('relacionada', models.CharField(blank=True, null=True)),
                ('visitas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ValoresJurisprudencia',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('idParametro', models.IntegerField()),
                ('idItemlista', models.IntegerField()),
                ('valor', models.CharField(blank=True, null=True)),
                ('parametro', models.CharField()),
                ('item', models.CharField(blank=True, null=True)),
                ('jurisprudencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarea_1_app.jurisprudencia')),
            ],
        ),
    ]
