## Requires Python 3
#### Instructions:
* pip install -r requirements.txt
* python manage.py shell
    * from main import *

*Once in manage.py shell, use the following commands* 

##### Customers:
* add_customer(first_name, last_name, email)
* list_customers(**kwargs)
    * no **kwargs returns all customers
    * first_name='<first name>'
    * last_name='<last name>'
    * email='<email>'
    * id=<primary key>
    
##### Subscriptions:
* add_subscription(customer_key, cost, tax, annual=True)
    * annual=False creates a quarterly subscription
* def list_subscriptions(**kwargs)
    * no **kwargs returns all customers
    * customer='<customer>' returns list of subscriptions for a customer 
    
#### The Model:
###### Customer:
    * first_name
    * last_name
    * email
    
###### Subscription:
    * customer (foreign key to Customer)
    * annual (Boolean -- False = quarterly)
    * cost (pre tax -- Integer)
    * tax (Integer)
    
From here functions can be added to main.py to operate further on the
current model, and the model can also be expanded by adding attributes
to the classes in models.py

###### If you expand the model, afterwards run
*  python manage.py makemigrations
* python manage.py migrate

###### to update the database