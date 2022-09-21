data ={
    1:{'name':'rehan','age':19,'Hoby':'Sing'},
    2: {'name':'Renaldi','age':29,'Hoby':'Foot Ball'},
    3: {'name':'Joni','age':43,'Hoby':'Eating'}
       }

for key,value in data.items():
    print(f'Data Ke {key}') # loop angka 1 dan 2

    for key2 in value:
        print(f'{key2} - {value[key2]}')



angka = {1,2,2,4}
print(angka)


