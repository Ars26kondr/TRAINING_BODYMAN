from django.db import models
    
class Slide(models.Model):
    title=models.CharField(max_length=200, blank=True)
    image=models.ImageField(upload_to='slides/')
    order=models.PositiveIntegerField(default=0)

    class Meta:
        ordering=['order']


    def __str__(self):
        return self.title

class Products(models.Model):
    name=models.CharField(max_length=200, blank=True)
    image=models.ImageField(upload_to='products/')
    brand=models.CharField(max_length=200, blank=True)
    price=models.PositiveIntegerField(default=0)
    discount=models.IntegerField()
    description=models.TextField()

    def GetSalePrice(self):
        return self.price*self.discount//100

    def __str__(self):
        return self.name
