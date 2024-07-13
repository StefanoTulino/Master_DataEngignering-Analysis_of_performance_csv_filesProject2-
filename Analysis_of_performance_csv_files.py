#[TRACCIA]

##	Analisi dell’andamento degli indici azionari S&P 500 ed EURO STOXX

#Due indici molto importanti che descrivono l’andamento dei mercati azionari sono l’indice S&P 500, che descrive l’azionario americano, e l’indice EURO STOXX 50 che descrive 
#l’azionario europeo.

#Partendo dai dataset relativi agli ultimi 10 anni di storico di questi indici (file sp500.csv per l’indice americano e euro50.csv per l’indice europeo), calcolare:
#*	il rendimento percentuale mensile e annuale, distinto per indice
#*	il rendimento medio giornaliero distinto per indice e per giorno della settimana
#*	individuare il giorno di maggiore rendimento giornaliero e di minore rendimento, distinto tra i due indici
#*	Calcolare il volume medio giornaliero dei due indici
#Per rendimento si intende la variazione percentuale del prezzo di chiusura rispetto al periodo precedente (per esempio, mensile o giornaliero).

#I dataset forniti hanno le seguenti colonne:
#	Date: la data in cui viene rilevato il prezzo
#	Open: il prezzo di apertura di quel giorno
#	High: il prezzo massimo raggiunto quel giorno
#	Low: il prezzo minimo raggiunto quel giorno
#	Close: il prezzo di chiusura di quel giorno
#	Volume: il numero di scambi di borsa avvenuti quel giorno

#---------------------------------------------------------------

# MAIN

import datetime as dt
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math

# Import myModule
import function1 as f

# NOTA: Senza di esso Warning(solo qui, su Jupyter ed in locale no) nel momento in cui prendo i giorni dalla data
# Warning --> <ipython-input-9-23cb58b85c2c>:50: SettingWithCopyWarning
pd.options.mode.copy_on_write = True

df_sp500= pd.read_csv("sp500.csv")
df_euro50= pd.read_csv("euro50.csv")


##############################        #1)

f.insert_column_new_date(df_sp500)
f.insert_column_new_date(df_euro50)
df_sp500.sort_values('NewDate')
df_euro50.sort_values('NewDate')

value_monthly_percentage_sp500 = f.value_monthly_percentage(df_sp500)
value_annual_percentage_sp500 = f.value_annual_percentage(df_sp500)
value_monthly_percentage_euro50 = f.value_monthly_percentage(df_euro50)
value_annual_percentage_euro50= f.value_annual_percentage(df_euro50)

series_monthly_sp500= pd.Series(value_monthly_percentage_sp500)
print("Rendimento Percentuale mensile df_sp500 mensile=\n", series_monthly_sp500.pct_change(),"\n")
series_annual_sp500= pd.Series(value_annual_percentage_sp500)
print("Rendimento Percentuale annuale di df_sp500= ",series_annual_sp500.pct_change(),"\n")
series_monthly_euro50= pd.Series(value_monthly_percentage_euro50)
print("Rendimento Percentuale mensile df_euro50 mensile=\n", series_monthly_euro50.pct_change(),"\n")
series_annual_euro50= pd.Series(value_annual_percentage_euro50)
print("Rendimento Percentuale annuale di df_euro50= ",series_annual_euro50.pct_change(),"\n")
print("\n#------------------------------------------------------------------ \n")


##############################        #2)

df_sp500["Average Daily"]= df_sp500["Close"].pct_change()
df_euro50["Average Daily"]= df_euro50["Close"].pct_change()
if math.isnan(df_sp500["Average Daily"].iloc[0]):
    df_sp500= df_sp500.dropna()
if math.isnan(df_euro50["Average Daily"].iloc[0]):
    df_euro50= df_euro50.dropna()
print("Rendimento medio giornaliero in PERCENTUALE per indice df_sp500=\n",df_sp500["Average Daily"],"\n")
print("Rendimento medio giornaliero in PERCENTUALE per indice df_euro50=\n",df_euro50["Average Daily"],"\n")

df_sp500["Day"]= df_sp500["NewDate"].dt.day_name()
df_euro50["Day"]= df_euro50["NewDate"].dt.day_name()
df_sp500_mean_daily= df_sp500.groupby(["Day"]).mean(numeric_only=True)
df_euro50_mean_daily= df_euro50.groupby(["Day"]).mean(numeric_only=True)

df_sp500_mean_daily['Volume'] = df_sp500_mean_daily['Volume'].astype(str)
df_euro50_mean_daily['Volume'] = df_euro50_mean_daily['Volume'].astype(str)
print("df_sp500_mean_daily=\n",df_sp500_mean_daily,"\n")
print("df_euro50_mean_daily=\n",df_euro50_mean_daily,"\n")
print("\n#------------------------------------------------------------------ \n")


##############################        #3)

day_max_value_sp500= df_sp500["Average Daily"].max()
boolean_mask_max_sp500=df_sp500['Average Daily']==day_max_value_sp500
print("df_sp500: Data,giorno e valore max=\n",df_sp500.loc[boolean_mask_max_sp500, ["Day","Date","Average Daily"]])
day_min_value_sp500= df_sp500["Average Daily"].min()
boolean_mask_min_sp500=df_sp500['Average Daily']==day_min_value_sp500
print("df_sp500: Data,giorno e valore min=\n",df_sp500.loc[boolean_mask_min_sp500,["Day","Date","Average Daily"]],"\n")

day_max_value= df_euro50["Average Daily"].max()
boolean_mask_max=df_euro50['Average Daily']==day_max_value
print("df_euro50: Data,giorno e valore max=\n",df_euro50.loc[boolean_mask_max, ["Day","Date","Average Daily"]])
day_min_value= df_euro50["Average Daily"].min()
boolean_mask_min=df_euro50['Average Daily']==day_min_value
print("df_euro50: Data,giorno e valore min=\n",df_euro50.loc[boolean_mask_min, ["Day","Date","Average Daily"]],"\n")
print("\n#------------------------------------------------------------------ \n")


##############################        #4)

mean_volume_daily_euro50= df_sp500["Volume"].mean()
mean_volume_daily_sp500= df_sp500["Volume"].mean()
print("mean_volume_daily_euro50= ",mean_volume_daily_euro50)
print("mean_volume_daily_sp500= ",mean_volume_daily_sp500)