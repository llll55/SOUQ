# Generated by Django 3.1.5 on 2021-01-11 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_variant'),
        ('product', '0012_auto_20210109_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDDesc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDISBastSeller',
            field=models.BooleanField(default=False, verbose_name='Best Seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDISNew',
            field=models.BooleanField(default=True, verbose_name='New Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product URL'),
        ),
    ]
