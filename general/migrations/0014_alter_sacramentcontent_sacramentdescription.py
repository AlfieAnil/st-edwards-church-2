# Generated by Django 4.1.1 on 2022-12-03 15:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_alter_sacramentcontent_sacramentdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sacramentcontent',
            name='SacramentDescription',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
