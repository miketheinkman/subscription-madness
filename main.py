from django.core.wsgi import get_wsgi_application
from customers.models import *

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
application = get_wsgi_application()


def add_customer(first_name, last_name, email):
    try:
        customer = Customer(first_name=first_name, last_name=last_name,
                            email=email)
        customer.save()
        return print('Customer added')
    except Exception as e:
        return print(e)


def add_subscription(customer_key, cost, tax, annual=True):
    try:
        customer = Customer.objects.get(pk=customer_key)
        subscription = Subscription(customer=customer, annual=annual,
                                    cost=cost, tax=tax)
        subscription.save()
        return print('Subscription added')
    except Exception as e:
        return print(e)


def list_customers(**kwargs):
    if kwargs:
        return Customer.objects.filter(**kwargs)
    return Customer.objects.all()


def list_subscriptions(**kwargs):
    if kwargs:
        return Subscription.objects.filter(**kwargs)
    return Subscription.objects.all()


def main():
    pass


if __name__ == '__main__':
    main()
