from django.db import models

class Card(models.Model):
    card_number = models.CharField(max_length=16)
    titular = models.CharField(max_length=100)
    due_date = models.DateField()

    def get_card_by_customer(self, id_customer):
        pass
