import requests
import time
import csv

URL = 'https://primairepopulaire.fr/get-signatures'
FILE = 'signature_timing.csv'

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

r = requests.get(URL)
nb_sign = int(r.json()['total'])
current_time = time.time()
data = [nb_sign, current_time]
append_list_as_row(FILE, data)
old_nb_sign = nb_sign
while(1):
    r = requests.get(URL)
    nb_sign = int(r.json()['total'])
    if(nb_sign > old_nb_sign):
        current_time = time.time()
        data = [nb_sign, current_time]
        append_list_as_row(FILE, data)
        old_nb_sign = nb_sign
    time.sleep(120)
