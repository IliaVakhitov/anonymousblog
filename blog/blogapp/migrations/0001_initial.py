# Generated by Django 3.0.2 on 2020-01-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=500)),
                ('date_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
