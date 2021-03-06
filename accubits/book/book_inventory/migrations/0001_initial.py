# Generated by Django 3.2.7 on 2021-09-06 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200, null=True)),
                ('author', models.CharField(max_length=200, null=True)),
                ('Book_count', models.IntegerField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('book_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_inventory.library')),
            ],
        ),
    ]
