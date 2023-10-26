from django.db import models

# Create your models here.
class Books(models.Model):
    ISBN = models.IntegerField();
    Book_Title = models.CharField(max_length=255);
    Book_Author = models.CharField(max_length=255);
    Year_Publication = models.IntegerField();
    Publisher = models.CharField(max_length=255);
    Book_Cover = "http://images.amazon.com/images/P/0195153448.01.MZZZZZZZ.jpg",
