from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    annual = models.BooleanField()
    cost = models.IntegerField()
    tax = models.IntegerField()

    def __str__(self):
        return str(self.customer) + " $" + str(int(self.cost)/100)
