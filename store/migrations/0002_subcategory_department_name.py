# Generated by Django 2.2.6 on 2019-10-24 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='department_name',
            field=models.OneToOneField(default='Dairy', on_delete=django.db.models.deletion.CASCADE, to='store.Department'),
        ),
    ]
