import csv

with open("nama.csv",'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    print("Nama dan Email")
    for row in csvReader:
        print(f"{row['first_name'] }- {row['email']}")
