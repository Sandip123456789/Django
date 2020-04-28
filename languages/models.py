from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=50)


    #To display the name of Language object
    def __str__(self):
        return self.name
