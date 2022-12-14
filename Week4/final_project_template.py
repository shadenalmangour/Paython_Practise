import pandas as pd 
import numpy as np

#Don't forget to change the directory before importing the file
movies_dataset=pd.read_excel("movie_metadata.xlsx")

#Question 1
#استخدام التابع shape، ما هو عدد الأسطر والأعمدة الموجودة في البيانات؟
print(movies_dataset.shape)

#Question 2

#Yes, each row for one movie

#Question 3

max_value=max(movies_dataset.duration)
print(max_value)


#Question 4

#result_movie_titles=movies_dataset["movie_title"] #هنا طلعت عناوين جميع الافلام
min_duration=min(movies_dataset.duration)
print(min_duration)#طلعت اقل مدة زمنية رقما
#looping through spesific DataFrames rows   
for row_label,row in movies_dataset.iterrows():
    if row["duration"]==min_duration: 
        print(row["movie_title"])
#Question 5
#Yes

duration_in_minutes=movies_dataset["duration"]/60
movies_dataset["duration_in_minutes"]=duration_in_minutes

#Question 6
x=movies_dataset['director_name']=="James Cameron"
df1=movies_dataset[x]
result=df1["director_name"].count()
print(result)

#Question 7
print(np.mean(movies_dataset["duration"]))

#Question 8
print(np.median(movies_dataset["duration"]))


#Question 9
y=np.logical_or(movies_dataset['language']=="Danish",
                movies_dataset['language']=="Dutch")

df2=movies_dataset[y]
result2=df2["language"].count()
print(result2)

#Question 10
z=movies_dataset['country']=="USA"
df3=movies_dataset[z]
result3=df3["country"].count()
print(result3)

#Question 11

movies_report_1=pd.pivot_table(df3,index=['is_colored']
                             ,values=['country']
                             ,aggfunc="count")

print(movies_report_1)
# =============================================================================

#Question 12

movies_report_2=pd.pivot_table(df3,index=['main_genre']
                                  ,values=["country",
                                           "imdb_score"]
                                  ,aggfunc={"country":"count",
                                            "imdb_score":np.mean,
                                           })


print(movies_report_2.sort_values("imdb_score"))


#Question 13

movies_report_3=pd.pivot_table(df3,index=['main_genre']
                                  ,values=["imdb_score",
                                           "budget"]
                                  ,aggfunc={"imdb_score":np.mean,
                                            "budget":np.mean,
                                           })


print(movies_report_3.sort_values("budget"))

#Question 14

movies_report_3=pd.pivot_table(df3,index=['main_genre']
                                  ,values="gross"
                                          
                                  ,aggfunc={"gross":np.mean })


print(movies_report_3.sort_values("gross"))



