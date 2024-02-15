from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    address = models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')

    def __str__(self):
        return self.name
