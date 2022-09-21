biodata = {
    'name' :'Andika',
    'umur' :27,
    'pekerjaan' :'Desainer',
    'Hoby' :'Nyanyi'
           }

biodata['Alamat'] = 'Bandar Lampung'
biodata['umur'] = 30

del (biodata['Hoby'])

for key , value in biodata.items():
    print(f'{key} - {value} ')

