# Generated by Django 4.1.1 on 2022-11-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_contactusreturns'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParishHubTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.TextField()),
                ('Day', models.CharField(max_length=9)),
            ],
        ),
    ]
