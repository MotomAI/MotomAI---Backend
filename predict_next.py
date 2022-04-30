import pandas as pd
import matplotlib.pyplot as plt
import base64

requested = 1
df = pd.read_csv('bq-results-20220430-091305-1651311205831.csv')

llistaguai = df.values.tolist()

llistachachix= []
llistachachiy = []

for row in llistaguai:
    if row[0] == requested:
        llistachachix.append(row[1])
        llistachachiy.append(row[2])

plt.plot(llistachachix, llistachachiy)
plt.savefig('graph.png')
with open("graph.png", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
print(my_string)
