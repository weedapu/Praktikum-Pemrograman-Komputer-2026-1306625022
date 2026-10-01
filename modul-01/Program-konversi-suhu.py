# Judul dan Identitas MHS
print("Tabel Konversi Suhu Celcius-Reamur-Fahrenheit")
print("Nama = Muhammad Gotzone Davu Quinn")
print("NIM = 1306625022")

#Input suhu awal, suhu akhir, dan selang suhu
print()
SuhuAwal = float(input("Masukkan suhu awal: "))
SuhuAkhir = float(input("Masukkan suhu akhir: "))
Selang = float(input("Masukkan selang suhu: "))

# Tabel konversi suhu
print("\nTabel Konversi Suhu:")
print("No | Celcius(°C) | Reamur(°R) | Fahrenheit(°F)")
print("-" * 45)

# Perulangan dan konversi suhu menggunakan while loop
C = SuhuAwal
No = 1
while C <= SuhuAkhir:
    F = (C * 9/5) + 32
    R = 4/5 * C
    print(f"{No:2d}  |  {C:8.1f}  |  {R:8.1f}  |  {F:8.1f}")
    C += Selang
    No += 1
print()
print("Selesai")