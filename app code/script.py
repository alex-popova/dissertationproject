from django.contrib import admin
from django.contrib.gis.geos import GEOSGeometry
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
import geopandas as gpd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import shapely.wkt
import gurobipy as gp
from gurobipy import GRB
from numpy import savetxt
from numpy import loadtxt

def optimizefunction(zone_input, investment_amount_input):
    '''
    df_expanded_sum = pd.read_csv('/Users/alexandrapopova/Downloads/NPV_map.csv')

    #load zone array
    loc_zones_array=loadtxt('/Users/alexandrapopova/Downloads/loc_zones_array.csv', delimiter=',')

    #load energy array
    energy_array_aw=loadtxt('/Users/alexandrapopova/Downloads/energy_array_aw.csv', delimiter=',')
    energy_array_ss=loadtxt('/Users/alexandrapopova/Downloads/energy_array_ss.csv',  delimiter=',')

    #load demand constraint array
    demand_array_aw=loadtxt('/Users/alexandrapopova/Downloads/demand_array_aw.csv', delimiter=',')
    demand_array_ss=loadtxt('/Users/alexandrapopova/Downloads/demand_array_ss.csv', delimiter=',')

    #add area constraint
    loc_area=loadtxt('/Users/alexandrapopova/Downloads/loc_area.csv', delimiter=',')

    #define model coefficients
    v_cost=df_expanded_sum['Vestas Investment Cost, kEUR'].to_numpy()
    n_cost=df_expanded_sum['Nordex Investment Cost, kEUR'].to_numpy()
    e_cost=df_expanded_sum['Enercon Investment Cost, kEUR'].to_numpy()
    s_cost=df_expanded_sum['SolarPV Investment Cost, kEUR'].to_numpy()
    v_NPV=df_expanded_sum['Vestas NPV, kEUR'].to_numpy()
    n_NPV=df_expanded_sum['Nordex NPV, kEUR'].to_numpy()
    e_NPV=df_expanded_sum['Enercon NPV, kEUR'].to_numpy()
    s_NPV=df_expanded_sum['SolarPV NPV, kEUR'].to_numpy()

    df_expanded_sum['mask']=np.where((df_expanded_sum['Zone']==zone_input), 1, 0)
    mask_array=df_expanded_sum['mask'].to_numpy()
    cost_max=investment_amount_input

    I=range(len(df_expanded_sum))
    E=range(4)
    Z=range(len(demand_array_aw))
    S=range(2)
    m=gp.Model()
    x = [[m.addVar(vtype=GRB.INTEGER) for e in E] for i in I] #binary variables
    for i in I:
        m.addConstr(((x[i][0]+x[i][1]+x[i][2])*0.8+x[i][3]*0.02) <= loc_area[i])
    for z in Z:
            m.addConstr(gp.quicksum((energy_array_aw[i][0]*x[i][0]+energy_array_aw[i][1]*x[i][1]+energy_array_aw[i][2]*x[i][2]+energy_array_aw[i][3]*x[i][3])*loc_zones_array[i][z] for i in I) <=demand_array_aw[z])
            m.addConstr(gp.quicksum((energy_array_ss[i][0]*x[i][0]+energy_array_ss[i][1]*x[i][1]+energy_array_ss[i][2]*x[i][2]+energy_array_ss[i][3]*x[i][3])*loc_zones_array[i][z] for i in I) <=demand_array_ss[z])
    m.addConstr(gp.quicksum(v_cost[i]*x[i][0] + n_cost[i]*x[i][1] + e_cost[i]*x[i][2] + s_cost[i]*x[i][3] for i in I)<=cost_max)
    m.setObjective(gp.quicksum(v_NPV[i] * x[i][0]*mask_array[i]+n_NPV[i]*x[i][1]*mask_array[i]+e_NPV[i]*x[i][2]*mask_array[i]+s_NPV[i]*x[i][3]*mask_array[i] for i in I), GRB.MAXIMIZE)
    m.optimize()

    solution_df=df_expanded_sum.copy()
    vars=m.getVars()
    Vestas_Location=np.array([])
    Nordex_Location=np.array([])
    Enercon_Location=np.array([])
    SolarPV_Location=np.array([])
    for v in range(m.NumVars):
        if v % 4 == 0:
            Vestas_Location=np.append(Vestas_Location,vars[v].x)
        else:
            if v % 4 == 1:
                Nordex_Location=np.append(Nordex_Location,vars[v].x)
            else:
                if v % 4 == 2:
                    Enercon_Location=np.append(Enercon_Location,vars[v].x)
                else:
                    SolarPV_Location=np.append(SolarPV_Location,vars[v].x)

    solution_df['Vestas_Location']=pd.Series(Vestas_Location)
    solution_df['Nordex_Location']=pd.Series(Nordex_Location)
    solution_df['Enercon_Location']=pd.Series(Enercon_Location)
    solution_df['SolarPV_Location']=pd.Series(SolarPV_Location)
    solution_df=solution_df.loc[(solution_df['Vestas_Location'] != -0) | (solution_df['Nordex_Location'] != -0) | (solution_df['Enercon_Location'] != 0) | (solution_df['SolarPV_Location'] != 0)]
    '''
    solution_df=pd.read_csv('/Users/alexandrapopova/Downloads/solution_Initial_2.csv')

    return (solution_df)
