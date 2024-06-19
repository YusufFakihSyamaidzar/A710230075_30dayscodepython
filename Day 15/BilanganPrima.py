def apakah_prima(bilangan):
    if bilangan > 1:
        for i in range(1, int(bilangan/2)+ 1):
            if(bilangan % i) == 0:
                print('Bukan Bilangan Prima')
                break
            else:
                print('Bilangan Prima')
    else:
        print('Bukan Bilangan Prima')

# Pemangilan Fungsi dan Meminta input
bilangan_input = int(input('Masukkan angka : '))
apakah_prima(bilangan_input)