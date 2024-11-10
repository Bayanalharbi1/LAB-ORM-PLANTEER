# Generated by Django 5.1.2 on 2024-11-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(default='images/default.png', upload_to='images/')),
                ('category', models.CharField(choices=[('TR', 'Trees'), ('SH', 'Shrubs'), ('HB', 'Herbs'), ('FL', 'Flowers'), ('VN', 'Vines')], default='TR', max_length=64)),
                ('is_edible', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
