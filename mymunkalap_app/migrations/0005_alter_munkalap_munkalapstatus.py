# Generated by Django 5.0.1 on 2024-02-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymunkalap_app', '0004_alter_munkalap_felhasznaltanyag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='munkalap',
            name='munkalapstatus',
            field=models.CharField(choices=[('enum_value_1', 'Aktív'), ('enum_value_2', 'Lezárt')], default='Aktív', max_length=20),
        ),
    ]
