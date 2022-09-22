nama = input("Namanya Siapa ? ")
monster = {'name':nama,'power':100}

def starGame():
    choise = input("Mau apa ? 1.Makan 2.Cek Status 3.Keluar ")
    if choise == '1':
        goEat()
    elif choise == '2':
        goStatus()
    elif choise == '3':
        goExit()
def goEat():
    print("Hmm Nyam Nyam Enak Sekali")
    monster['power'] += 100
    starGame()

def goStatus():
    print(f"Jumlah Power Kamu {monster['power']}")
    starGame()

def goExit():
    print("By By........")
    print(monster)



   

starGame()