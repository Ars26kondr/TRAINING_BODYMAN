from django.db import models
class Game(models.Model): 
    Name=models.CharField(max_length=100)
    Price=models.FloatField()
    Year=models.DateField()
    Rating=models.FloatField()
    Creator=models.CharField(default="Unknown", max_length=100, blank=True, null=True)
    Platforms=models.CharField(default="Unknown", max_length=100, blank=True, null=True)
    Discount=models.IntegerField(blank=True, null=True)
    Subscription=models.BooleanField(blank=True, null=True, default=False)
    Icon=models.ImageField(default='Unknown', null=True, blank=True, upload_to='IMG/')
    @property
    def GetSalePrice(self):
        return self.Price*self.Discount//100

# Create your models here.
