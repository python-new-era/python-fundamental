file = open('data.txt','w')

def daftar(newText):
    file.write(f"\n{newText}")
    


def askUser():
    daftar(input("Ketik apa mau mu ? : "))


askUser()