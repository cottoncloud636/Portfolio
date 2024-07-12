#models.py is for storing data, related to the DB
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
path1 = 'static/assets/media/'
class Project(models.Model): #inheriting functionality and features provided by the Model class from the 
                             #django.db.models
    screenshot = models.ImageField(upload_to=path1, blank=True, null=True)
    title = models.CharField(max_length=20)
    description = models.TextField()
    youtube = models.URLField(blank=True, null=True)

    def __str__ (self): #this method returns the title name in admin interface, w/o this, it will return an "object" literally
        return self.title

    def formatted_description(self):
        return mark_safe(self.description)

class Like(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Likes for {self.project.title}"


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    msg = models.TextField()

    def __str__(self):
        return self.name
