# Generated by Django 2.1.7 on 2019-02-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0003_auto_20190226_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]