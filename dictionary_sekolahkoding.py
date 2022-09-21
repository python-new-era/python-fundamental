data= {
    'name' : 'Herman',
    'age'  : 18,
    'Hoby' : 'nynyi'
}


data['name'] = 'jihan'
data['perkerjaan'] = 'desainer'

del data['perkerjaan']


for key ,value in data.items():
    print(f'{key} : {value}')



