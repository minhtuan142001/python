# Generated by Django 4.2.1 on 2023-06-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DanhMuc',
            fields=[
                ('DanhMuc_id', models.AutoField(primary_key=True, serialize=False)),
                ('TenDM', models.CharField(max_length=50)),
            ],
        ),
    ]