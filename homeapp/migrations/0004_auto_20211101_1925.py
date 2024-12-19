# Generated by Django 3.2.8 on 2021-11-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_auto_20211101_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='recruited',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AlterField(
            model_name='company',
            name='minpercentage',
            field=models.DecimalField(decimal_places=2, default=35, max_digits=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]