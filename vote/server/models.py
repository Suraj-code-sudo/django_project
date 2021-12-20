from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
# Create your models here.
class server(models.Model):
    event = models.CharField(max_length=120)
    op1 = models.CharField(max_length=120)
    op2 = models.CharField(max_length=120)
    op3 = models.CharField(max_length=120)
    op4 = models.CharField(max_length=120)
    op5 = models.CharField(max_length=120)
    op6 = models.CharField(max_length=120)
    op7 = models.CharField(max_length=120)
    op8 = models.CharField(max_length=120)
    op9 = models.CharField(max_length=120)
    op10 = models.CharField(max_length=120)
    def __str__(self):
        return f"{self.op1} {self.op2} {self.op3} {self.op4} {self.op5} {self.op6} {self.op7} {self.op8} {self.op9} {self.op10}"


    
class testing(models.Model):
    test = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.test}"
