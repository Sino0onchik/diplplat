from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)
    image = models.FileField(upload_to='images/category/')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class Product(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/product/')
    price = models.PositiveIntegerField(blank=True, default=0)
    price_rent = models.PositiveIntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


class ImgProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/product/')

