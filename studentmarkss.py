import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("studentmarkss.csv")
print(df)
# plt.pie(df["sum"]labels=df["students"])
plt.pie(df["average"],labels=df["students"],autopct='%1.1f%%')
plt.title("student marks graph")
plt.show()