# Generated by Django 4.1.7 on 2023-03-17 16:39

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('stock', models.CharField(choices=[('in_stock', 'В наличии'), ('out_of_stock', 'Нет в наличии')], max_length=50)),
                ('quantity', models.CharField(choices=[('wholesale', 'Оптом'), ('retail', 'В розницу')], max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='category.subcategory')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
