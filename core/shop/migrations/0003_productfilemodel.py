# Generated by Django 4.2.16 on 2024-10-04 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productmodel_manufactureddata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='product/files/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_files', to='shop.productmodel')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]