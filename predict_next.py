import pandas as pd
import matplotlib.pyplot as plt

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
plt.show()