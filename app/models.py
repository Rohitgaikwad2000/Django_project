from django.db import models

# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=50)
    MF_date = models.DateField()
    product_no = models.CharField(max_length =15)
    is_deleted = models.BooleanField(default = False)


    def __str__(self):
        return f"{self.Name}"
    

    class Meta:
        db_table = "app"




