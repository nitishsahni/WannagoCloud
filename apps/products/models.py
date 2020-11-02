from django.db import models


class Riserva(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price_dollars = models.DecimalField(max_digits=19, decimal_places=2)
    price_aed = models.DecimalField(max_digits=19, decimal_places=2)
    selling_price = models.DecimalField(max_digits=19, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DRaaS(models.Model):
    name = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=19, decimal_places=2)
    cost_price = models.DecimalField(max_digits=19, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'DRaaS'
        verbose_name_plural = 'DRaaS'

    def __str__(self):
        return self.name



class IaaS(models.Model):
    name = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=19, decimal_places=4)
    cost_price = models.DecimalField(max_digits=19, decimal_places=4)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'IaaS'
        verbose_name_plural = 'IaaS'

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    name = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=19, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.name