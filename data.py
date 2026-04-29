import pandas as pd
data ={
    "calories":[420,300,200],
    "duration":[50,40,45]
}
df=pd.DataFrame(data)
print(df)

print(df.loc[0])


import pandas as pd
data={
    "students":['a','b','c','d','e','f','g','h','i','j'],
    "marks":[60,80,90,67,97,85,94,58,84,70]
}
df=pd.DataFrame(data)
print(df)
print(df.loc[5])
print(df.loc[6])