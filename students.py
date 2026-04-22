import numpy as np
import matplotlib.pyplot as plt
students = ["anu","abhi","athu","malu","devu"]
marks = [75,90,95,75,60]
plt.xlabel("students")
plt.ylabel("marks")
plt.title("student VS marks")
plt.scatter(students,marks)
plt.grid()
plt.show()
