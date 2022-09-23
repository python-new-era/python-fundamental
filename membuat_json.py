import json

# data={}
# data['member'] = [
#  {"nama" :"Songoku","Jurus":"Kamehameha","Power":100},
#  {"nama" :"Yip","Jurus":"Wincun","Power":400},
#  {"nama" :"Satan","Jurus":"Tinju","Power":50}]
#
# with open('member.txt','w') as membersfile:
#     json.dump(data,membersfile)


with open('member.txt','r') as memberFile:
    data = json.load(memberFile)
    for member in data['member']:
        print(f" Nama {member['nama']} punya jurus {member['Jurus']}")

