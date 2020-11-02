from django.db import models

from ..master.models import Partner, Customer
from ..products.models import IaaS, DRaaS, Riserva, Subscriptions


class IaaS_DRaaS_Form(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    requested_items = models.CharField(max_length=1000)


class Riserva_Form(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    riserva = models.ForeignKey(Riserva, on_delete=models.CASCADE)
    requested_items = models.CharField(max_length=1000)
