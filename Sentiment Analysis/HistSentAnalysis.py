import json
import pandas as pd
import math
from matplotlib import pyplot as plt
import pprint
import numpy as np
import seaborn as sns

#listaY = [12500, 5365, 11344, 53649, 24312]
listaYPositive = [9818, 4278, 9071, 39996, 17866]
listaYNegative = [2682, 1087, 2273, 13653, 6446]

listaX = ["2018", "2019", "2020", "2021", "2022"]
xpos = np.arange(len(listaX))

barWidth = 0.4
plt.bar(listaX, listaYNegative, color = "red", label = "Negative")
plt.bar(listaX, listaYPositive, bottom = listaYNegative, color="green", label = "Positive")
plt.legend()
plt.title("Positive/Negative content of Submissions through the years")
plt.xlabel("Years")
plt.ylabel("Number of Submissions")
#plt.text("2018", 500, "21%")
#plt.text("2018", 10000, "79%")
#plt.text("2019", 200, "20%")
#plt.text("2019", 3000, "80%")
#plt.text("2020", 500, "20%")
#plt.text("2020", 9000, "80%")
#plt.text("2021", 10000, "26%")
#plt.text("2021", 51000, "74%")
#plt.text("2022", 4000, "27%")
#plt.text("2022", 22000, "83%")

plt.show()