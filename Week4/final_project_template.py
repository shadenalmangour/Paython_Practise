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
#ما هي أطول مدة فيلم موجودة في البيانات؟
max_value=max(movies_dataset.duration)
print(max_value)


#Question 4
#ما هو اسم أقصر فيلم موجود في البيانات؟
#result_movie_titles=movies_dataset["movie_title"] 
min_duration=min(movies_dataset.duration)
print(min_duration)#طلعت اقل مدة زمنية رقما

#looping through spesific DataFrames rows   
for row_label,row in movies_dataset.iterrows():
    if row["duration"]==min_duration: 
        print(row["movie_title"])


#Question 5
#الكود التالي يقوم باضافة عمود جديد إلى البيانات اسمه 
# "duration_in_minutes"
#يحتوي على مدة الفيلم الواحد بالساعات

duration_in_minutes=movies_dataset["duration"]/60
movies_dataset["duration_in_minutes"]=duration_in_minutes

#Yes

#ما هو عدد الأفلام التي قام بإخراجها المخرج
#James Cameron

#Question 6
x=movies_dataset['director_name']=="James Cameron"
df1=movies_dataset[x]
result=df1["director_name"].count()
print(result)

#ما هو المتوسط الخاص بمدة الأفلام الموجودة في البيانات
#Question 7
print(np.mean(movies_dataset["duration"]))


#ما هو الوسيط الخاص بمدة الأفلام الموجودة في البيانات
#Question 8
print(np.median(movies_dataset["duration"]))


#ما هو عدد الأفلام التي لغتها هي
#"Danish" أو "Dutch" 
#Question 9
y=np.logical_or(movies_dataset['language']=="Danish",
                movies_dataset['language']=="Dutch")

df2=movies_dataset[y]
result2=df2["language"].count()
print(result2)

#ما هو عدد الأفلام التي تم انتاجها في "USA"
#Question 10
z=movies_dataset['country']=="USA"
df3=movies_dataset[z]
result3=df3["country"].count()
print(result3)

#قم بانشاء تقرير يظهر عدد الأفلام الملونة وعدد الأفلام بالأبيض والأسود التي تم انتاجها في "USA"
#بالاعتماد على هذا  التقرير ما هو عدد الأفلام الملونة وعدد الأفلام بالأبيض والأسود؟
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
#"main genre" قم بانشاء تقرير يظهر عدد الأفلام ومتوسط تقييمات الأفلام حسب ال 
# التي تم انتاجها في "USA"
#بالاعتماد على هذا التقرير
#ما هي أعلى ثلاثة genres حسب متوسط التقييمات؟

movies_report_3=pd.pivot_table(df3,index=['main_genre']
                                  ,values=["imdb_score",
                                           "budget"]
                                  ,aggfunc={"imdb_score":np.mean,
                                            "budget":np.mean,
                                           })


print(movies_report_3.sort_values("budget"))

#Question 14
#قم بانشاء تقرير يظهر متوسط تقييمات الأفلام ومتوسط تكلفة الأفلام  حسب ال "main genre" 
#التي تم انتاجها في "USA"
#بالاعتماد على هذا التقرير ما هي أعلى ثلاثة genres حسب متوسط تكلفة الفيلم؟
movies_report_3=pd.pivot_table(df3,index=['main_genre']
                                  ,values="gross"
                                          
                                  ,aggfunc={"gross":np.mean })


print(movies_report_3.sort_values("gross"))



