
from django.db import models

class AddMoney(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amountAdd = models.IntegerField()
    nameAdd = models.CharField(max_length=225)
    def __str__(self):
        return f"{self.nameAdd}"
class SubMoney(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amountSub = models.IntegerField()
    nameSub = models.CharField(max_length=225)
    def __str__(self):
        return f"{self.nameSub}"