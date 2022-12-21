# Generated by Django 4.1.3 on 2022-12-05 08:10

from django.db import migrations, models
import django.db.models.deletion
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.category'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_completion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(validators=[todo.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='todo',
            name='has_been_done',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]