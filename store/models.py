from django.db import models
from django.contrib.auth.models import AbstractUser


class StoreUser(AbstractUser):

    def __str__(self):
        return "{}".format(self.username)


class Categories(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media', default='categories.jpg', blank=True, null=True)

    def __str__(self):
        return "{} category".format(self.title)


class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', default='product.jpg', blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=1)
    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return "{} with price {}".format(self.title, self.price)


class Order(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
