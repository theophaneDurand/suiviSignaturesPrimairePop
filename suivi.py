import requests
import time
import csv

URL = 'https://primairepopulaire.fr/get-signatures'
FILE = 'signature_timing.csv'

header = ['nb_new_signs', 'time']

r = requests.get(URL)
count = 20
i = 0
file = open(FILE, 'w')
with open(FILE, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    nb_sign = int(r.json()['total'])
    current_time = time.time()
    data = [nb_sign, current_time]
    writer.writerow(data)
    old_nb_sign = nb_sign
    while(count > i):
        r = requests.get(URL)
        nb_sign = int(r.json()['total'])
        if(nb_sign > old_nb_sign):
            current_time = time.time()
            data = [[nb_sign - old_nb_sign, current_time]]
            writer.writerow(data)
            i += 1
            old_nb_sign = nb_sign
        time.sleep(1)