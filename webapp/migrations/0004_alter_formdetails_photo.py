# Generated by Django 4.2.7 on 2024-02-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_userid_formdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetails',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
