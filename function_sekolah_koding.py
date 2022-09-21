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

