# Meminta inputan angka 
a = int(input("Masukkan Angka pertama : "))
b = int(input("Masukkan Angka kedua : "))

# Mencetak value boolean dari kedua angka
print(a == b)
print(a > b)
print(a < b)

# Mencetak hasil perbandingan kedua angka
if a == b:
    print("a bernilai sama dengan b")
elif a > b:
    print("a lebih besar dari b")
elif a < b:
    print("a lebih kecil dari b")
else:
    pass