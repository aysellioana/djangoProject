# Generated by Django 3.2.7 on 2021-10-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='cnp',
            field=models.IntegerField(),
        ),
    ]