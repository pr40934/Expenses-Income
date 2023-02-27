from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class db(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product = models.CharField(max_length=200)
    amount = models.IntegerField()
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product  
    
    class Meta:
        ordering = ['complete']
