from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    STATUS = (
        ('In progress', 'In progress'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order')
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, default='In progress')

    def __str__(self):
        return self.product.name
