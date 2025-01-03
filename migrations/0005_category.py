# Generated by Django 5.1.4 on 2024-12-31 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0004_alter_women_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=244, unique=True)),
            ],
        ),
    ]
