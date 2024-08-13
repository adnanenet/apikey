from django.db import models

class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    numbers = models.IntegerField()

    def __str__(self):
        return self.email

class Sumrush(models.Model):
    account = models.ForeignKey(Account, related_name='sumrush', on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    difficulty = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.IntegerField()
    cpc = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.keyword

class Google(models.Model):
    keyword = models.CharField(max_length=255)

    def __str__(self):
        return self.keyword
