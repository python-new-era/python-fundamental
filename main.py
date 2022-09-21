nama_member = ['sinka','renaldi','sofyan','jemi','thomson']



nama_member.append('Joni')





print('Implementasi Pop \n')

member = nama_member.pop(-1)
for i in range(0,len(nama_member)):
    print(nama_member[i])

print(f'nama member yang hilang adalah : {member}')




print('list konherensif')
nama_member = ['sinka','renaldi','sofyan','jemi','thomson']

del nama_member[2:4]

for i in range(0,len(nama_member)):
    print(nama_member[i])




