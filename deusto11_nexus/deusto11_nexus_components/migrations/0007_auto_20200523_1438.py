# Generated by Django 3.0.5 on 2020-05-23 12:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('deusto11_nexus_components', '0006_auto_20200523_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(default='XXX', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='telefone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+41520000000', max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_nick',
            field=models.CharField(default='XXX', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='provider_telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+41520000000', max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='set_number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
