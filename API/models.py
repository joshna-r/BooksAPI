from django.db import models
import re
from django.core.exceptions import ValidationError


def nameFiledValidator(value):
    s = str(value)
    if len(s)== 13:
        return value
    else:
        raise ValidationError("ISBN Number Must be 13 digit")


# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True)
    isbn = models.CharField('ISBN', max_length=13,help_text="Enter 13 digit ISBN Number", unique=True, 
                             validators=[nameFiledValidator])
    date_of_publication = models.DateField(null=True, blank=True)



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    wishlist = models.ManyToManyField(book,blank=True)
    # wishlist = models.ForeignKey('book', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name}'

