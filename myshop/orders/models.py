from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from shop.models import Product
from users.models import Profile
# Create your models here.


class Order(models.Model):
    user = models.OneToOneField(Profile,
                                on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE,
                              null=False)
    products = models.ForeignKey(Product,
                                 related_name='order_items',
                                 on_delete=models.CASCADE,
                                 null=False)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                validators=[
                                    MinValueValidator(Decimal('0.01'))
                                ])
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
