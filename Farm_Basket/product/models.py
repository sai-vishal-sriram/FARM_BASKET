from django.db import models

# Create your models here.

class Productmaster(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productmaster'
