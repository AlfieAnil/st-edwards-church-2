# Generated by Django 4.1.1 on 2022-12-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0017_baptismform_cw_gender_2_baptismform_cw_name_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baptismform',
            name='cw_gender_2',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='cw_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='cw_name_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='cw_practicing',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='cw_practicing_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='cw_religion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='cw_religion_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='baptismform',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
