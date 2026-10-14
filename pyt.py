import numpy as np
import pandas as pd

# Check NumPy version
print("NumPy Version:", np.__version__)

# Ex:2

notes=np.array([12, 15, 14, 16, 10])
print("Array:", notes)
print("Array:", type(notes))

print("-----------------------------------------------------------")
# ex:3

print(np.mean(notes));
print(np.max(notes))
print(np.min(notes))
notes_bonus = notes +1 
print(notes_bonus)
print("-----------------------------------------------------------")

# EX4

image = np.array([
    [0,0,255],
    [0,128,2255],
    [255,255,0]
])
print(image)
print(image.shape)
print(image[1,2])
image[0,0]=200
print(image)
print("-----------------------------------------------------------")

# Ex5
data = {
    "Nom": ["Ahmed", "Sara", "Youssef", "Imane"],
    "Age": [20, 21, 19, 22],
    "Note": [15, 17, 12, 19]
}
df = pd.DataFrame(data)
print(df)
