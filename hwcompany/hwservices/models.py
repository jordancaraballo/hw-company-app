from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from django.core.validators import DecimalValidator

# Create your models here.
class Manufacturer(models.Model):
    MAN_CODE     = models.AutoField(primary_key=True)
    MAN_COMPANY  = models.CharField(max_length=50)
    MAN_STREET   = models.CharField(max_length=30)
    MAN_CITY     = models.CharField(max_length=30)
    MAN_STATE    = models.CharField(max_length=30)
    MAN_ZIP      = models.IntegerField() # 5
    MAN_AREACODE = models.IntegerField() # 3
    MAN_PHONE    = models.CharField(max_length=8)
    MAN_ACCNUM   = models.CharField(max_length=16) # 16

class Brand(models.Model):
    BRAND_LEVEL_CHOICES = (
        ('premium', 'premium'),
        ('mid-level', 'mid-level'),
        ('entry-level', 'entry-level'),
    )
    BRAND_ID    =  models.AutoField(primary_key=True)
    BRAND_NAME  = models.CharField(max_length=30)
    BRAND_LEVEL = models.CharField(max_length=30,choices=BRAND_LEVEL_CHOICES)
    MAN_CODE    = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Model(models.Model):
    MODEL_NUM     = models.AutoField(primary_key=True)
    MODEL_JETS    = models.IntegerField()
    MODEL_MOTORS  = models.IntegerField()
    MODEL_HP      = models.IntegerField()
    MODEL_SRP     = models.DecimalField(max_digits=8, decimal_places=2, validators=[DecimalValidator]) # los validators fastidian buscar forma de validar
    MODEL_HWRP    = models.DecimalField(max_digits=8, decimal_places=2, validators=[DecimalValidator])
    MODEL_WEIGTH  = models.DecimalField(max_digits=8, decimal_places=2, validators=[DecimalValidator])
    MODEL_WATCAP  = models.DecimalField(max_digits=8, decimal_places=2, validators=[DecimalValidator])
    MODEL_SEATCAP = models.IntegerField()
    BRAND_ID      = models.ForeignKey(Brand, on_delete=models.CASCADE)
