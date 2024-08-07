import json
import pandas as pd
import math
from matplotlib import pyplot as plt
import pprint
import numpy as np
import seaborn as sns

listaYSubjective = [24, 24, 22, 24, 25]
listaYNotSubjective = [76, 76, 78, 76, 75]

listaX = ["2018", "2019", "2020", "2021", "2022"]

plt.rcParams.update({'font.size': 18})

barWidth = 0.4
ticksY = ["0", "20%", "40%", "60%", "80%", "100%"]
ax = plt.axes()
plt.bar(listaX, listaYNotSubjective, color = "grey", label = "Not subjective")
plt.bar(listaX, listaYSubjective, bottom = listaYNotSubjective, color="blue", label = "Subjective")
ax.set_yticklabels(ticksY)
plt.legend(loc="best")
# plt.title("Subjectivity of Submissions through the years")
plt.xlabel("Years")
plt.ylabel("Total Submissions")

plt.show()