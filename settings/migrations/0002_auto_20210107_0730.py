# Generated by Django 3.1.5 on 2021-01-07 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Varuabt',
            new_name='Variant',
        ),
        migrations.AlterModelOptions(
            name='variant',
            options={'verbose_name': 'Variant', 'verbose_name_plural': 'Variants'},
        ),
    ]
