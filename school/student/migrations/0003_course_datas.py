# Generated by Django 4.1.5 on 2023-05-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_course_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200)),
                ('fees', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
