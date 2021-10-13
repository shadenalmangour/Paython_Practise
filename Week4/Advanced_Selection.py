import pandas as pd
import numpy as np

#importing data 
soccer_dataset=pd.read_excel("soccer_dataset.xlsx")

#Step1
print(soccer_dataset["home_team"])

#Step2
print(soccer_dataset["home_team"]=="spain")

x=soccer_dataset["home_team"]=="spain"

#Step3
spain_dataset=soccer_dataset[x]


y=np.logical_and(soccer_dataset["home_team"]=="England",
               soccer_dataset["home_score"]>=7)

england_data=soccer_dataset[y]

#looping through all DataFrames rows
for label, row_data in soccer_dataset.iterrows():
    print(label,row_data)
    
#looping through spesific DataFrames rows   
for label, row_data in soccer_dataset.iterrows():
    print(label,row_data["home_team"])
    
#looping through spesific DataFrames rows   
for label, row_data in soccer_dataset.iterrows():
    soccer_dataset.loc[label,"new_col"]="fun"