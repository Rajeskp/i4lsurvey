from django.db import models

class Items(models.Model):
    content = models.TextField()
    
class opt(models.Model):
    ans = models.TextField()
    ques = models.TextField()
    team = models.TextField()