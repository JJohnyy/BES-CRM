# Generated by Django 3.2.13 on 2022-06-03 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20220603_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]