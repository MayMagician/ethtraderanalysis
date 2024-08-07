import time
import requests
import datetime
import json
import re
import matplotlib.pyplot as plt

f = open('submissionsFrom2018.json')

# ritorno l'oggetto json come dizionario
data = json.load(f)

sub2018 = 0
sub2019 = 0
sub2020 = 0
sub2021 = 0
sub2022 = 0

# itero tutte le submissions
for i in data['submissions']:
    if re.search("\A2018", i["time"]) is not None:
        sub2018 = sub2018 + 1
    if re.search("\A2019", i["time"]) is not None:
        sub2019 = sub2019 + 1
    if re.search("\A2020", i["time"]) is not None:
        sub2020 = sub2020 + 1
    if re.search("\A2021", i["time"]) is not None:
        sub2021 = sub2021 + 1
    if re.search("\A2022", i["time"]) is not None:
        sub2022 = sub2022 + 1

# chiudo il file
f.close()

myDict = {"2018": sub2018, "2019": sub2019, "2020": sub2020, "2021": sub2021, "2022": sub2022}
myJson = json.dumps(myDict)
with open("provona.json", "a") as outfile:
    outfile.write(myJson)

# i dati risultanti sono coerenti con i dati che pushshift dà a questo indirizzo https://api.pushshift.io/reddit/search/submission/?subreddit=ethtrader&metadata=true&size=0&after=1577836800&before=1609459200

# inizia il lavoro sul grafico

# x-coordinates of left sides of bars 
left = [0, 10, 20, 30, 40]
  
# heights of bars
height = [sub2018, sub2019, sub2020, sub2021, sub2022]
  
# labels for bars
tick_label = ['2018', '2019', '2020', '2021', '2022']

plt.rcParams.update({'font.size': 18})
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 3, color = ['green', 'green', 'green', 'red', 'green'])
  
# naming the x-axis
plt.xlabel('Years')
# naming the y-axis
plt.ylabel('Submissions')
# plot title (non lo mettiamo tanto nella tesi mettiamo il nome dell'immagine)
# plt.title('Submissions/Years chart')
  
# function to show the plot
plt.show()