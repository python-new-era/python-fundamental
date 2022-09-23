import csv

rows = [
 {"nama" :"Songoku","Jurus":"Kamehameha","Power":100},
 {"nama" :"Yip","Jurus":"Wincun","Power":400},
 {"nama" :"Satan","Jurus":"Tinju","Power":50}]

with open('dataok.csv','a') as csvfile:
    fields = ['nama','Jurus','Power']
    writer = csv.DictWriter(csvfile,fieldnames=fields)

    writer.writeheader()
    writer.writerow(rows)