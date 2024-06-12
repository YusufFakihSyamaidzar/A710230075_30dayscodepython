print('Selamat Datang di Aplikasi Cat')
jumlah_dinding = int(input('Masukkan Jumlah Dinding = '))
print('-'* 40)
total_luas = 0

for i in range (1, jumlah_dinding + 1):
    print(f'Dinding {i}')
    panjang = input('Panjang (m) = ')
    lebar = input('Lebar (m) = ')
    luas = int(panjang) * int(lebar)
    print(f'Luas (m2) = {luas}')
    print('-'* 40)
    total_luas += luas

print(f'Total Luas Dinding (m2) = {total_luas}')
print(f'Total Biaya Pengecatan = Rp.{total_luas * 35000}')
print('-'* 40)