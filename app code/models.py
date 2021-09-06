#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import MultiPolygon
from django.contrib.gis.geos import Polygon

# Create your models here.

class NPVMap(models.Model):
    NPV=models.FloatField()
    geom=models.MultiPolygonField()

    def __str__(self):
        return self.PolId

    class Meta:
        verbose_name_plural='NPVMap'




class ZoneMap(models.Model):
    zone= models.CharField(max_length=100)
    price= models.FloatField()
    geom=models.MultiPolygonField()

    def __str__(self):
        return self.LineId

    class Meta:
        verbose_name_plural='ZoneMap'

class WindMap(models.Model):
    speed= models.CharField(max_length=100)
    colorcode= models.CharField(max_length=100)
    geom=models.MultiPolygonField()

    def __str__(self):
        return self.LineId

    class Meta:
        verbose_name_plural='WindMap'

class OptimisationResMap(models.Model):
    V_number= models.FloatField()
    N_number= models.FloatField()
    E_number= models.FloatField()
    P_number= models.FloatField()
    V_NPV= models.FloatField()
    N_NPV= models.FloatField()
    E_NPV= models.FloatField()
    P_NPV= models.FloatField()
    V_Inv= models.FloatField()
    N_Inv= models.FloatField()
    E_Inv= models.FloatField()
    P_Inv= models.FloatField()
    V_IRR= models.FloatField()
    N_IRR= models.FloatField()
    E_IRR= models.FloatField()
    P_IRR= models.FloatField()
    V_PBP= models.FloatField()
    N_PBP= models.FloatField()
    E_PBP= models.FloatField()
    P_PBP= models.FloatField()

    geom=models.PolygonField()

    def __str__(self):
        return self.LineId

    class Meta:
        verbose_name_plural='OptimisationResMap'
