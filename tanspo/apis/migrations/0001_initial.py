# Generated by Django 2.1.7 on 2019-02-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=4)),
                ('home', models.CharField(max_length=100)),
                ('work', models.CharField(max_length=100)),
            ],
        ),
    ]
