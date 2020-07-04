import pandas as pd
import random as r
import numpy as np

s= pd.Series(np.random.randint(60,100,[10]))
s2=pd.Series(np.random.choice(['A','B','C'],[10]),)
print(s)
s3= pd.Series([
    'Rahul',
    'Karthik',
    'Vineeth',
    "Vishal",
    "Kumar",
    "Keerthi",
    "Surya",
    
    "Geetha",
    "Rekha",
    'Sanjay'
])
print(s2)
df=pd.concat([s3,s2,s],axis=1)
df.columns=['Name','Section','Marks']
print(df)
s4=pd.Series(np.random.randint(20,25,[5]),dtype='int')
s5=pd.Series([
    'David',
    'John',
    'Stefan',
    'Nick',
    'Joseph'
])
df2=pd.concat([s5,s4],axis=1)
df2.columns=['Name','Age']
print(df2)

with open("a.html", 'w') as _file:
    _file.write(df.head().to_html() + "\n\n" + df2.head().to_html())
