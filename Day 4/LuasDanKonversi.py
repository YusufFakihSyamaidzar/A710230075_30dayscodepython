# Meminta inputan Panjang dan Lebar
panjang = int(input('Masukkan panjang (dalam cm) : '))
lebar = int(input('Masukkan lebar (dalam cm) : '))

# Menghitung Luas Persegi Panjang dalam centimeter(cm)
luas = panjang * lebar

# Konversi ukuran dari centimeter(cm) ke meter(m)
panjang2 = panjang / 100
lebar2 = lebar / 100
luas2 = luas / 10000

# Mencetak hasil luas dan konversi
print(f'Panjang Persegi Panjang setelah di konversi adalah {panjang2} m')
print(f'Lebar Persegi Panjang setelah di konversi adalah {lebar2} m')
print(f"Luas Persegi Panjang adalah {luas} cm atau {luas2} m")