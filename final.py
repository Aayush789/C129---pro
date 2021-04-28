import csv

dataset_1 = []
dataset_2 = []

with open("dataset_1.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:

        dataset_1.append(row)

with open("dataset_2_sorted.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:

        dataset_2.append(row)

header_1 = dataset_1[0]

dwarfstars_data_1 = dataset_1[1:]

header_2 = dataset_2[0]

dwarfstars_data_2 = dataset_2[1:]

headers = header_1 + header_2

dwarfstars_data = []

for index, data_row in enumerate(dwarfstars_data_1):
    dwarfstars.append(dwarfstars_data_1[index] + dwarfstars_data_2[index])

with open("final.csv","a+") as f:
   csvwriter = csv.writer(f)
   csvwriter.writerow(headers)
   csvwriter.writerows(dwarfstars_data)