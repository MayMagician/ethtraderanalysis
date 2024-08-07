import time
import requests
import datetime
import json
import re
import matplotlib.pyplot as plt

f = open('allComments.json')

# ritorno l'oggetto json come dizionario
data = json.load(f)

com2018 = 0
com2019 = 0
com2020 = 0
com2021 = 0
com2022 = 0

# itero tutti i commenti
for i in data['comments']:
    if re.search("\A2018", i["time"]) is not None:
        com2018 = com2018 + 1
    if re.search("\A2019", i["time"]) is not None:
        com2019 = com2019 + 1
    if re.search("\A2020", i["time"]) is not None:
        com2020 = com2020 + 1
    if re.search("\A2021", i["time"]) is not None:
        com2021 = com2021 + 1
    if re.search("\A2022", i["time"]) is not None:
        com2022 = com2022 + 1

# chiudo il file
f.close()

myDict = {"2018": com2018, "2019": com2019, "2020": com2020, "2021": com2021, "2022": com2022}
myJson = json.dumps(myDict)
with open("commentsPerYearResults.json", "w") as outfile:
    outfile.write(myJson)

# inizia il lavoro sul grafico

# x-coordinates of left sides of bars 
left = [0, 10, 20, 30, 40]
  
# heights of bars
height = [com2018, com2019, com2020, com2021, com2022]
  
# labels for bars
tick_label = ['2018', '2019', '2020', '2021', '2022']
  
plt.rcParams.update({'font.size': 18})

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 3, color = ['green', 'green', 'green', 'red', 'green'])

plt.ticklabel_format(style="plain", axis="y")

# naming the x-axis
plt.xlabel('Years')
# naming the y-axis
plt.ylabel('Comments')
# plot title (non lo mettiamo tanto nella tesi mettiamo il nome dell'immagine)
# plt.title('Comments/Years chart')
  
# function to show the plot
plt.show()