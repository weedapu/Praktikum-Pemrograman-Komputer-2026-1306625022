#Judul dan Identitas MHS
print("=" * 50)
print("PROGRAM FAKTOR BILANGAN".center(50))
print("=" * 50)
print()
print("Nama = Muhammad Gotzone Davu Quinn")
print("NIM = 202310374")
print()
while True:
#Input bilangan
    n = int(input("Masukkan sembarang bilangan: "))
    if n == 0:
        break 
    faktor = []
#Perulangan untuk mencari faktor bilangan
    for i in range(1, n + 1):
        if n % i == 0:
            faktor.append(i)
    print("Faktor dari", n, "adalah:", faktor)
print()
print("Selesai")   
            


    