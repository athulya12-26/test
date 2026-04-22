import numpy as np
import matplotlib.pyplot as plt
x=np.array([5,7,2,9,3])
y=np.array([7,3,9,5,2])
plt.plot(x,y,marker='o')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("simple line plot")
plt.grid()
plt.show()