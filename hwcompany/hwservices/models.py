from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    MAN_CODE     = models.AutoField(primary_key=True)
    MAN_COMPANY  = models.CharField(max_length=50)
    MAN_STREET   = models.CharField(max_length=30)
    MAN_CITY     = models.CharField(max_length=30)
    MAN_STATE    = models.CharField(max_length=30)
    MAN_ZIP      = models.IntegerField(max_length=5)
    MAN_AREACODE = models.IntegerField(max_length=3)
    MAN_PHONE    = models.CharField(max_length=8)
    MAN_ACCNUM   = models.IntegerField(max_length=16)

class Brand(models.Model):
    BRAND_ID    =  models.AutoField(primary_key=True)
    BRAND_NAME  = models.CharField(max_length=30)
    BRAND_LEVEL = models.CharField(max_length=30)
    MAN_CODE    = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Model(models.Model):
    MODEL_NUM     = models.AutoField(primary_key=True)
    MODEL_JETS    = models.IntegerField(max_length=10)
    MODEL_MOTORS  = models.IntegerField(max_length=10)
    MODEL_HP      = models.IntegerField(max_length=10)
    MODEL_SRP     = models.DecimalField(max_digits=8, decimal_places=2)
    MODEL_HWRP    = models.DecimalField(max_digits=8, decimal_places=2)
    MODEL_WEIGTH  = models.DecimalField(max_digits=8, decimal_places=2)
    MODEL_WATCAP  = models.DecimalField(max_digits=8, decimal_places=2)
    MODEL_SEATCAP = models.IntegerField(max_length=10)
    BRAND_ID      = models.ForeignKey(Brand, on_delete=models.CASCADE)
