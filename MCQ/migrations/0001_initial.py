# Generated by Django 3.1.1 on 2020-09-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=200)),
                ('o_1', models.CharField(max_length=100)),
                ('o_2', models.CharField(max_length=100)),
                ('o_3', models.CharField(max_length=100)),
                ('o_4', models.CharField(max_length=100)),
                ('ans', models.CharField(max_length=100)),
            ],
        ),
    ]