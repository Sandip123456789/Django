from django.db import models

# Create your models here.
class Paradigm(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    #To display the name of Language object
    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
