player1  = {'name':'Goku','Power':300}
player2 = {'name':'Gohan','Power':500}

def latihan(player):
    player['Power'] += 100


def serang(attack,defender):
    if attack['Power'] > defender['Power']:
        print(f"Serangan kamu bagus {attack['name']}")
    else:
        print(f"Serangan mu tak berguna {attack['name']}")


latihan(player1)
latihan(player1)
latihan(player1)
latihan(player1)
latihan(player2)
serang(player1,player2)



print("Banyak Banyakan Duit")

programmer = {'name':'lina','Gaji':300}
desainer   = {'name':'Linda','Gaji':400}

def lebur(kerja):
    kerja['Gaji'] += 100


def aduDuit(progam,desain):
    if progam['Gaji'] > desain['Gaji']:
        print(f"{progam['name']} Kamu Programmer Duit mu lebih banyak dari pada {desain['name']}")
    else:
        print(f"{progam['name']} Kamu Programer Duit mu sedikit ")


lebur(programmer)
lebur(programmer)
aduDuit(programmer,desainer)



