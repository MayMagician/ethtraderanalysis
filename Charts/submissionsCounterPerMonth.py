import time
import requests
import datetime
import json
import re
import matplotlib.pyplot as plt

f = open('submissionsFrom2018.json')

# ritorno l'oggetto json come dizionario
data = json.load(f)

jan2018 = 0
feb2018 = 0
mar2018 = 0
apr2018 = 0
may2018 = 0
jun2018 = 0
jul2018 = 0
aug2018 = 0
sep2018 = 0
oct2018 = 0
nov2018 = 0
dec2018 = 0
jan2019 = 0
feb2019 = 0
mar2019 = 0
apr2019 = 0
may2019 = 0
jun2019 = 0
jul2019 = 0
aug2019 = 0
sep2019 = 0
oct2019 = 0
nov2019 = 0
dec2019 = 0
jan2020 = 0
feb2020 = 0
mar2020 = 0
apr2020 = 0
may2020 = 0
jun2020 = 0
jul2020 = 0
aug2020 = 0
sep2020 = 0
oct2020 = 0
nov2020 = 0
dec2020 = 0
jan2021 = 0
feb2021 = 0
mar2021 = 0
apr2021 = 0
may2021 = 0
jun2021 = 0
jul2021 = 0
aug2021 = 0
sep2021 = 0
oct2021 = 0
nov2021 = 0
dec2021 = 0
jan2022 = 0
feb2022 = 0
mar2022 = 0
apr2022 = 0
may2022 = 0
jun2022 = 0
jul2022 = 0
aug2022 = 0
sep2022 = 0
oct2022 = 0
nov2022 = 0
dec2022 = 0

# itero tutte le submissions
for i in data['submissions']:
    if re.search("\A2018-01", i["time"]) is not None:
        jan2018 = jan2018 + 1
    if re.search("\A2018-02", i["time"]) is not None:
        feb2018 = feb2018 + 1
    if re.search("\A2018-03", i["time"]) is not None:
        mar2018 = mar2018 + 1
    if re.search("\A2018-04", i["time"]) is not None:
        apr2018 = apr2018 + 1
    if re.search("\A2018-05", i["time"]) is not None:
        may2018 = may2018 + 1
    if re.search("\A2018-06", i["time"]) is not None:
        jun2018 = jun2018 + 1
    if re.search("\A2018-07", i["time"]) is not None:
        jul2018 = jul2018 + 1
    if re.search("\A2018-08", i["time"]) is not None:
        aug2018 = aug2018 + 1
    if re.search("\A2018-09", i["time"]) is not None:
        sep2018 = sep2018 + 1
    if re.search("\A2018-10", i["time"]) is not None:
        oct2018 = oct2018 + 1
    if re.search("\A2018-11", i["time"]) is not None:
        nov2018 = nov2018 + 1
    if re.search("\A2018-12", i["time"]) is not None:
        dec2018 = dec2018 + 1
    if re.search("\A2019-01", i["time"]) is not None:
        jan2019 = jan2019 + 1
    if re.search("\A2019-02", i["time"]) is not None:
        feb2019 = feb2019 + 1
    if re.search("\A2019-03", i["time"]) is not None:
        mar2019 = mar2019 + 1
    if re.search("\A2019-04", i["time"]) is not None:
        apr2019 = apr2019 + 1
    if re.search("\A2019-05", i["time"]) is not None:
        may2019 = may2019 + 1
    if re.search("\A2019-06", i["time"]) is not None:
        jun2019 = jun2019 + 1
    if re.search("\A2019-07", i["time"]) is not None:
        jul2019 = jul2019 + 1
    if re.search("\A2019-08", i["time"]) is not None:
        aug2019 = aug2019 + 1
    if re.search("\A2019-09", i["time"]) is not None:
        sep2019 = sep2019 + 1
    if re.search("\A2019-10", i["time"]) is not None:
        oct2019 = oct2019 + 1
    if re.search("\A2019-11", i["time"]) is not None:
        nov2019 = nov2019 + 1
    if re.search("\A2019-12", i["time"]) is not None:
        dec2019 = dec2019 + 1
    if re.search("\A2020-01", i["time"]) is not None:
        jan2020 = jan2020 + 1
    if re.search("\A2020-02", i["time"]) is not None:
        feb2020 = feb2020 + 1
    if re.search("\A2020-03", i["time"]) is not None:
        mar2020 = mar2020 + 1
    if re.search("\A2020-04", i["time"]) is not None:
        apr2020 = apr2020 + 1
    if re.search("\A2020-05", i["time"]) is not None:
        may2020 = may2020 + 1
    if re.search("\A2020-06", i["time"]) is not None:
        jun2020 = jun2020 + 1
    if re.search("\A2020-07", i["time"]) is not None:
        jul2020 = jul2020 + 1
    if re.search("\A2020-08", i["time"]) is not None:
        aug2020 = aug2020 + 1
    if re.search("\A2020-09", i["time"]) is not None:
        sep2020 = sep2020 + 1
    if re.search("\A2020-10", i["time"]) is not None:
        oct2020 = oct2020 + 1
    if re.search("\A2020-11", i["time"]) is not None:
        nov2020 = nov2020 + 1
    if re.search("\A2020-12", i["time"]) is not None:
        dec2020 = dec2020 + 1
    if re.search("\A2021-01", i["time"]) is not None:
        jan2021 = jan2021 + 1
    if re.search("\A2021-02", i["time"]) is not None:
        feb2021 = feb2021 + 1
    if re.search("\A2021-03", i["time"]) is not None:
        mar2021 = mar2021 + 1
    if re.search("\A2021-04", i["time"]) is not None:
        apr2021 = apr2021 + 1
    if re.search("\A2021-05", i["time"]) is not None:
        may2021 = may2021 + 1
    if re.search("\A2021-06", i["time"]) is not None:
        jun2021 = jun2021 + 1
    if re.search("\A2021-07", i["time"]) is not None:
        jul2021 = jul2021 + 1
    if re.search("\A2021-08", i["time"]) is not None:
        aug2021 = aug2021 + 1
    if re.search("\A2021-09", i["time"]) is not None:
        sep2021 = sep2021 + 1
    if re.search("\A2021-10", i["time"]) is not None:
        oct2021 = oct2021 + 1
    if re.search("\A2021-11", i["time"]) is not None:
        nov2021 = nov2021 + 1
    if re.search("\A2021-12", i["time"]) is not None:
        dec2021 = dec2021 + 1
    if re.search("\A2022-01", i["time"]) is not None:
        jan2022 = jan2022 + 1
    if re.search("\A2022-02", i["time"]) is not None:
        feb2022 = feb2022 + 1
    if re.search("\A2022-03", i["time"]) is not None:
        mar2022 = mar2022 + 1
    if re.search("\A2022-04", i["time"]) is not None:
        apr2022 = apr2022 + 1
    if re.search("\A2022-05", i["time"]) is not None:
        may2022 = may2022 + 1
    if re.search("\A2022-06", i["time"]) is not None:
        jun2022 = jun2022 + 1
    if re.search("\A2022-07", i["time"]) is not None:
        jul2022 = jul2022 + 1
    if re.search("\A2022-08", i["time"]) is not None:
        aug2022 = aug2022 + 1
    if re.search("\A2022-09", i["time"]) is not None:
        sep2022 = sep2022 + 1
    if re.search("\A2022-10", i["time"]) is not None:
        oct2022 = oct2022 + 1
    if re.search("\A2022-11", i["time"]) is not None:
        nov2022 = nov2022 + 1
    if re.search("\A2022-12", i["time"]) is not None:
        dec2022 = dec2022 + 1

# chiudo il file
f.close()

# inizia il lavoro sul grafico

# x-coordinates of left sides of bars 
left = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590]

# heights of bars
height = [jan2018, feb2018, mar2018, apr2018, may2018, jun2018, jul2018, aug2018, sep2018, oct2018, nov2018, dec2018, jan2019, feb2019, mar2019, apr2019, may2019, jun2019, jul2019, aug2019, sep2019, oct2019, nov2019, dec2019, jan2020, feb2020, mar2020, apr2020, may2020, jun2020, jul2020, aug2020, sep2020, oct2020, nov2020, dec2020, jan2021, feb2021, mar2021, apr2021, may2021, jun2021, jul2021, aug2021, sep2021, oct2021, nov2021, dec2021, jan2022, feb2022, mar2022, apr2022, may2022, jun2022, jul2022, aug2022, sep2022, oct2022, nov2022, dec2022]

# labels for bars
tick_label = ['2018', '', '', '', '', '', '', '', '', '', '', '', '2019', '', '', '', '', '', '', '', '', '', '', '', '2020', '', '', '', '', '', '', '', '', '', '', '', '2021', '', '', '', '', '', '', '', '', '', '', '','2022', '', '', '', '', '', '', '', '', '', '', '2023']

plt.rcParams.update({'font.size': 18})

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 2, color = ['green', 'red'])

# naming the x-axis
plt.xlabel('Months')
# naming the y-axis
plt.ylabel('Submissions')
# plot title (non lo mettiamo tanto nella tesi mettiamo il nome dell'immagine)
# plt.title('Submissions/Months chart')
  
# function to show the plot
plt.show()