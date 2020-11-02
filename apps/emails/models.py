from django.db import models


class EmailTemplate(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField(max_length=5000)
    attachment_required = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)