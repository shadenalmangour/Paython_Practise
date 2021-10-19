import pandas as pd
import numpy as np

soccer_dataset=pd.read_excel("soccer_dataset.xlsx")

country_report=pd.pivot_table(soccer_dataset, 
                              index="country", 
                              values="city", 
                              aggfunc="count")
print(country_report)
tournment_report=pd.pivot_table(soccer_dataset,index="tournament",
                                values=["home_score",
                                        "away_score",
                                        "city"],
                                aggfunc={"home_score":np.sum,
                                         "away_score":np.sum,
                                         "city":"count"})

print(tournment_report)
