from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from category.models import Subcategory
from deals.models import Deals
from django.core.validators import RegexValidator

User = get_user_model()


class Product(models.Model):
    STOCK_CHOICES = (
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Нет в наличии')
    )
    QUANTITY_CHOICES = (
        ('wholesale', 'Оптом'),
        ('retail', 'В розницу')
    )
    owner = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products')
    title = models.CharField(max_length=150)
    stock = models.CharField(choices=STOCK_CHOICES, max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    quantitytype = models.CharField(choices=QUANTITY_CHOICES, max_length=50, default=QUANTITY_CHOICES[1])
    description = RichTextField()
    image = models.ImageField(upload_to='images')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Subcategory, related_name='products', on_delete=models.RESTRICT)
    phonenumberregex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phonenumber = models.CharField(validators=[phonenumberregex], max_length=16, unique=True)
    deal = models.ForeignKey(Deals, related_name='products', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Favorites(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ['owner', 'product']