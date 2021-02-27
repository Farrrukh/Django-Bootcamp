# Generated by Django 3.1.6 on 2021-02-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
