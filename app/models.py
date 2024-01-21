from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_name=models.CharField(primary_key=True,max_length=28)
    def __str__(self):
        return self.Topic_name
    
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Url=models.URLField()
    Email=models.EmailField('hai@gmail.com')
    def __str__(self):
        return self.Name
    
class AccessRecord(models.Model):
    Name=models.OneToOneField(Webpage,on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=24)
    def __str__(self):
        return self.Author

