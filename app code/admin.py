from django.contrib import admin
from django.contrib.gis.geos import GEOSGeometry
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
import geopandas as gpd
from pandas import ExcelWriter
from pandas import ExcelFile
import shapely.wkt

from capacityapp.models import NPVMap
from capacityapp.models import ZoneMap
from capacityapp.models import WindMap
from capacityapp.models import OptimisationResMap
from capacityapp.script import optimizefunction

# Register your models here.

class CapacityPlannerAdmin(LeafletGeoAdmin):
    pass

admin.site.register(NPVMap, CapacityPlannerAdmin)
admin.site.register(ZoneMap, CapacityPlannerAdmin)
admin.site.register(WindMap, CapacityPlannerAdmin)
admin.site.register(OptimisationResMap, CapacityPlannerAdmin)

df_NPV_reader = pd.read_csv('/Users/alexandrapopova/Downloads/NPV_polygons_map.csv')
df_zones_reader = pd.read_csv('/Users/alexandrapopova/Downloads/zone_map.csv')
df_wind_reader = pd.read_csv('/Users/alexandrapopova/Downloads/wind_map_2.csv')
df_optimisation_reader = pd.read_csv('/Users/alexandrapopova/Downloads/solution_Initial_2.csv')

for index, row in df_NPV_reader.iterrows():
    NPV=row['average_we']
    geom=row['WKT']

    NPVMap(NPV=NPV, geom=geom).save()


for index, row in df_zones_reader.iterrows():
    zone= row['zone']
    price = row['average_price_average_price']
    geom=row['WKT']

    ZoneMap(zone=zone, price=price, geom=geom).save()

for index, row in df_wind_reader.iterrows():
    speed= row['title']
    colorcode = row['fill']
    geom=row['WKT']

    WindMap(speed=speed, colorcode=colorcode, geom=geom).save()

for index, row in df_optimisation_reader.iterrows():

    V_number=row['Vestas_Location']
    N_number= row['Nordex_Location']
    E_number= row['Enercon_Location']
    P_number= row['SolarPV_Location']
    V_NPV= row['Vestas NPV, kEUR']
    N_NPV= row['Nordex NPV, kEUR']
    E_NPV= row['Enercon NPV, kEUR']
    P_NPV= row['SolarPV NPV, kEUR']
    V_Inv= row['Vestas Investment Cost, kEUR']
    N_Inv= row['Nordex Investment Cost, kEUR']
    E_Inv= row['Enercon Investment Cost, kEUR']
    P_Inv= row['SolarPV Investment Cost, kEUR']
    V_IRR= row['Vestas IRR']
    N_IRR= row['Nordex IRR']
    E_IRR= row['Enercon IRR']
    P_IRR= row['SolarPV IRR']
    V_PBP= row['Vestas Payback']
    N_PBP= row['Nordex Payback']
    E_PBP= row['Enercon Payback']
    P_PBP= row['SolarPV Payback']
    geom=row['geometry']

    OptimisationResMap(V_number=V_number, N_number=N_number, E_number=E_number, P_number=P_number, V_NPV=V_NPV, N_NPV=N_NPV, E_NPV=E_NPV, P_NPV=P_NPV, V_Inv=V_Inv, N_Inv=N_Inv, E_Inv=E_Inv, P_Inv=P_Inv, V_IRR=V_IRR, N_IRR=N_IRR, E_IRR=E_IRR, P_IRR=P_IRR,V_PBP=V_PBP, N_PBP=N_PBP, E_PBP=E_PBP, P_PBP=P_PBP, geom=geom).save()
