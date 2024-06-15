from djongo import models

class Person(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
