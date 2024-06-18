from django.db import models

from users.models import User


class Client(models.Model):
    account_number = models.CharField(max_length=20, primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    inn = models.CharField(max_length=12)
    status = models.CharField(max_length=20, default='Не в работе')
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_responsible_full_name(self):
        if self.responsible:
            return self.responsible.full_name
        else:
            return "No Responsible Assigned"