# Generated by Django 4.1.6 on 2023-02-09 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parties_where_im_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
