from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, null=True)

    age = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    email = models.CharField(max_length=200, null=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

