from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect
from django.urls import reverse


class User(AbstractUser):
    pass

    def login_redirect(self):
        if self.is_staff:
            return redirect(reverse('admin:index'))
        else:
            return redirect('pricing_index')


class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.company_name
