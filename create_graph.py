import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime

x = []
y = []

with open('./signature_timing.csv') as file:
    csvFile = csv.reader(file)
    next(csvFile)
    for lines in csvFile:
        y.append(int(lines[0]))
        time = datetime.datetime.fromtimestamp(int(lines[1].split('.')[0]))
        x.append(time)
        

plt.plot(x, y, '-')
plt.gcf().autofmt_xdate()
plt.title("{} signatures actuellement".format(y[-1]))
plt.xlabel("Jour et heure de la journée")
plt.ylabel("Nombre de signatures")
plt.savefig('{}.png'.format(x[-1].strftime("%m%d")))
plt.show()
