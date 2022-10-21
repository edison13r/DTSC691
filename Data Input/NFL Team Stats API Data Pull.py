# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:49:46 2022

@author: rolle
"""

import requests
import pandas as pd 

url = "https://nfl-team-stats1.p.rapidapi.com/v1/nfl/teamStats"

years = ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', 
         '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
         '2016', '2017', '2018', '2019', '2020', '2021', '2022']

for i in years:
    querystring = {"year":i}
    
    headers = {
    	"X-RapidAPI-Key": "861b47d282mshdb2f94136f01420p1c6335jsndab80ec1a344",
    	"X-RapidAPI-Host": "nfl-team-stats1.p.rapidapi.com"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = response.text
    
    #data2 = data.decode("utf-8")
    data2 = pd.DataFrame.from_dict(eval(data))
    with pd.ExcelWriter(r"C:\Users\rolle\OneDrive\Documents\MS Data Science\DTSC 691\Proposal\Data\NFL_team_stats.xlsx",
                        engine="openpyxl", mode='a') as writer:
        data2.to_excel(writer, sheet_name=i)