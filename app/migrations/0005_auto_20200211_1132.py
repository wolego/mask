# Generated by Django 2.1.1 on 2020-02-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pv',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='contact',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
