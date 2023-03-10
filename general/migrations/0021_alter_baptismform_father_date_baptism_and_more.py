# Generated by Django 4.1.1 on 2022-12-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0020_baptismform_practicing_church_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baptismform',
            name='father_date_baptism',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='godparent_confirmation_date_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='godparent_dob_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='mother_date_baptism',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='mother_date_confirmation',
            field=models.DateField(blank=True),
        ),
    ]
