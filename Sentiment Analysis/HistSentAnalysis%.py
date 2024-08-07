import json
import pandas as pd
import math
from matplotlib import pyplot as plt
import pprint
import numpy as np
import seaborn as sns

listaYNegative = [21, 20, 20, 26, 27]
listaYPositive = [79, 80, 80, 74, 73]

listaX = ["2018", "2019", "2020", "2021", "2022"]

plt.rcParams.update({'font.size': 26})

barWidth = 0.4
ticksY = ["0", "20%", "40%", "60%", "80%", "100%"]
ax = plt.axes()
plt.bar(listaX, listaYNegative, color = "red", label = "Negative")
plt.bar(listaX, listaYPositive, bottom = listaYNegative, color="green", label = "Positive")
ax.set_yticklabels(ticksY)
plt.legend(loc=(-0.15, -0.142))
# plt.title("Positive/Negative content of Submissions in the years in percentage")
plt.xlabel("Years")
plt.ylabel("Total Submissions")

plt.show()