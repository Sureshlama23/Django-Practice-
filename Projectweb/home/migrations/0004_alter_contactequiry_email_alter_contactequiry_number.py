# Generated by Django 5.0 on 2024-01-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_contact_contactequiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactequiry',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactequiry',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]