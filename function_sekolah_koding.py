def jumlah_buku():
    for i in range(0,3):
        print(f"Baca Buku Ke {i}")

jumlah_buku()


print("Fungsi Penjumlahan")
def penjumlahan(a,b):
    print(a*b)

penjumlahan(4,4)

print("Function parameter dan loop")

def hitung(a,b):
    for i in range(0,5):
        print(f"Jumlah a + b adalah {a+b*3}")


hitung(20,10)

print("Funsgi dan return")

def cal(a,b):
    return a+b

hasil = cal(10,40)

print(hasil + 20)


print("Keyword argument")

def printData(nam,hoby):
    print(f"Nama : {nam} Hoby : {hoby}")


printData(nam ="joni" ,hoby='nyanyi')


print('*agrs dan **Kwargs')

def cobaprint(*args):
    for jeneng in args:
        print(jeneng)

cobaprint('Joni' ,'Ronan')


print('*agrs dan **Kwargs')

def cobaprint2(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

cobaprint2(nama ="joni",hoby="berenang")


def cobaArgs(*args):
    for name in args:
        print(name)

cobaArgs("doiana",'rumain')

print("\nCoba Kwargs")

def cobaKwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} - {value}")

cobaKwargs(nama ="joni",alamat="metro",pekerjaan="desainer")





