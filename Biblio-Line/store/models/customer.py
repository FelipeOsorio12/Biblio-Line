from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    date = models.DateField()
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    city = models.IntegerField(default=0)
    description = models.CharField(max_length=250)
    is_subscribed = models.IntegerField(default=0)

    #to save the data
    def register(self):
        self.save()

    def update(self, data):
        self.first_name = data[0]
        self.last_name = data[1]
        self.phone = data[2]
        self.email = data[3]
        self.address = data[4]
        self.description = data[5]
        self.save()

    def change_password(self, new_password):
        self.password = new_password
        self.save()

    def tosubscribe(self):
        self.is_subscribed = 1
        self.save()

    @staticmethod
    def get_customer_by_id(id):
        try:
            return Customer.objects.get(id = id)
        except:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
