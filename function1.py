import datetime as dt
import pandas as pd
import numpy as np
import math


"""
Public method for calculate the monthly percentage return on a dataframe passed as a parameter
Parameter: df is a DataFrame
Return: a list containing the values ​​for each month
"""
def value_monthly_percentage(df) -> list:
    periods_monthly = pd.to_datetime(df['NewDate']).dt.to_period('M')
    values_monthly = round(df.groupby(periods_monthly)['Close'].transform('last'),2)    
    values= values_monthly.unique()
    list_values_monthly= values.tolist()

    return list_values_monthly



"""
Public method for calculate the annual percentage return on a dataframe passed as a parameter
Parameter: df is a DataFrame
Return: a list containing the values ​​for each year
"""
def value_annual_percentage(df) -> list:
    periods_year = pd.to_datetime(df['NewDate']).dt.to_period('Y')
    values_annual = round(df.groupby(periods_year)['Close'].transform('last'),2)    
    values= values_annual.unique()
    list_values_annual= values.tolist()    
    return list_values_annual



"""
Public method that insert a new column into dataframe
Parameter: df is a DataFrame
"""
def insert_column_new_date(df):
    for index, row in df.iterrows():
    # Used slicing function to cut the last part, i.e -04:00
        date_selected= dt.datetime.strptime(row.iloc[0][:19],"%Y-%m-%d %H:%M:%S")
        if index==0:
            df.insert(2, "NewDate",date_selected , True)
        else:
            df.loc[index, 'NewDate'] = date_selected