import random

#memilih angka random
angka_random = random.randint(1, 100)

print('Selamat Datang di Game Tebak Angka!')
print('\nSaya telah memilih angka dari 1 sampai 100')
print('Anda punya 5 kesempatan untuk menebaknya')

kesempatan = 5

while kesempatan > 0:
    tebakan = int(input('Tebak Angka :'))

    if tebakan == angka_random:
        print(f'Selamat! Anda berhasil menebak angka dengan benar ({angka_random}) dalam {6-kesempatan}x kesempatan')
        break

    elif tebakan > angka_random:
        print(f'Angka terlalu tinggi. Kesempatan Anda tinggal {kesempatan-1}x lagi')

    elif tebakan < angka_random:
        print(f'Angka terlalu rendah. Kesempatan Anda tinggal {kesempatan-1}x lagi')

    kesempatan -= 1

    if kesempatan == 0:
        print(f'Kesempatan Anda sudah habis angkanya adalah {angka_random}')        