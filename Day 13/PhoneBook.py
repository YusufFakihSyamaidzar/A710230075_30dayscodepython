# Mendapatkan nama dan nomor telepon dari pengguna
kontak = {}
for i in range(1, 5):
 nama = input('Masukkan nama teman {}: '.format(i))
 no_hp = input('Masukkan nomor HP teman {}: '.format(i))
 kontak[nama] = no_hp

#kata asli
kata = 'Phone Book'

#menampilkan hasil
print()
print(kata.center(50))
print()
for no, nama in enumerate(kontak, start=1):
    print('{}. [{}] = [{}]'.format(no, nama, kontak[nama]))