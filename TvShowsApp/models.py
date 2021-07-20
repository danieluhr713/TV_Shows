from django.db import models
from datetime import date, datetime
# Create your models here.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors["title"] = "Movie title should be at least 5 characters long"
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors["description"] = "Description should be at least 10 characters long or not exist"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be more than 2 characters long."
        if datetime.strptime(postData['releaseDate'], '%Y-%m-%d') > datetime.now():
            errors["dateTime"] = 'Release Date should be in the past'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

