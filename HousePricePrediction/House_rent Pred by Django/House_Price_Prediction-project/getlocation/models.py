from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Divisions(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class District(models.Model):
    division = models.ForeignKey(Divisions, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
    
class Upazila(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
