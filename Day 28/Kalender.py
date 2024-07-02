import calendar

def main():
    print("Selamat datang di Kalender Sederhana")
    while True:
        print("\nSilakan pilih operasi yang ingin Anda lakukan:")
        print("1. Tampilkan kalender bulan ini")
        print("2. Tampilkan kalender tahun ini")
        print("3. Keluar")

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            # Tampilkan kalender bulan ini
            tampilkan_kalender_bulan_ini()
        elif choice == '2':
            # Tampilkan kalender tahun ini
            tampilkan_kalender_tahun_ini()
        elif choice == '3':
            # Keluar dari program
            print("Terima kasih telah menggunakan kalender ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")

def tampilkan_kalender_bulan_ini():
    # Dapatkan tahun dan bulan saat ini
    tahun_sekarang = calendar.datetime.date.today().year
    bulan_sekarang = calendar.datetime.date.today().month

    # Tampilkan kalender untuk bulan ini
    print("\nKalender untuk bulan ini:")
    print(calendar.month(tahun_sekarang, bulan_sekarang))

def tampilkan_kalender_tahun_ini():
    # Dapatkan tahun saat ini
    tahun_sekarang = calendar.datetime.date.today().year

    # Tampilkan kalender untuk tahun ini
    print("\nKalender untuk tahun ini:")
    print(calendar.calendar(tahun_sekarang))

if __name__ == "__main__":
    main()
