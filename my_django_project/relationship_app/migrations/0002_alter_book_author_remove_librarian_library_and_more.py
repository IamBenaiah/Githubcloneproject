# Generated by Django 5.1.6 on 2025-03-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.RemoveField(
            model_name='librarian',
            name='library',
        ),
        migrations.RemoveField(
            model_name='library',
            name='books',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]
