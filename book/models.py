from django.db import models

# Create your models here.
class Books(models.Model):
    ISBN = models.IntegerField();
    Book_Title = models.CharField(max_length=255);
    Book_Author = models.CharField(max_length=255);
    Year_Publication = models.IntegerField();
    Publisher = models.CharField(max_length=255);
    Book_Cover = models.CharField(max_length=255),
