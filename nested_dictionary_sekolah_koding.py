data ={
    1:{'name':'rehan','age':19,'Hoby':'Sing'},
    2: {'name':'Renaldi','age':29,'Hoby':'Foot Ball'}
       }

for key,value in data.items():
    print(f'Data Ke {key}') # loop angka 1 dan 2

    for key2 in value:
        print(f'{key2} - {value[key2]}')



