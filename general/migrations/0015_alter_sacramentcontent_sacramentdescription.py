# Generated by Django 4.1.1 on 2022-12-03 15:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_alter_sacramentcontent_sacramentdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sacramentcontent',
            name='SacramentDescription',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
