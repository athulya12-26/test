import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("studentsmarks.csv")
print(df)
plt.pie(df["maths"],df["english"],df["accountancy"],df["economics"])
plt.title("student marks graph")
plt.show()