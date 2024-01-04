# Generated by Django 5.0 on 2024-01-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone_number', models.CharField(max_length=11)),
                ('instrument_type', models.CharField(choices=[('Piano', 'Piano'), ('Mridangam', 'Mridangam'), ('Flute', 'Flute'), ('Violin', 'Violin')], max_length=10)),
            ],
        ),
    ]
