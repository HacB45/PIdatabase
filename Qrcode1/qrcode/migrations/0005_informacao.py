# Generated by Django 3.1.6 on 2021-02-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode', '0004_avarias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacao', models.CharField(max_length=255)),
                ('idmaquina', models.CharField(default='anything', max_length=10)),
            ],
        ),
    ]
