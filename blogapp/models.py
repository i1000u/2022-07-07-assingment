from pickle import FALSE
from django.db import models



# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField(blank = FALSE)
    writer = models.CharField(max_length = 20, default = '천우')
  
    HAPPY = 'HAPPY'
    SAD = 'SAD'
    ANGRY = 'ANGRY'
    JEALOUS = 'JEALOUS'
    CHOICES = [(HAPPY,'happy'),(SAD,'sad'),(ANGRY,'angry'),(JEALOUS,'jealous')]
    today_feeling = models.CharField(max_length = 10, choices = CHOICES, null = True) 
   

    def __str__(self):
        return self.title
