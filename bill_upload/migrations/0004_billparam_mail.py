# Generated by Django 4.2.4 on 2023-08-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_upload', '0003_remove_billparam_user_remove_billupload_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='billparam',
            name='mail',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
    ]
