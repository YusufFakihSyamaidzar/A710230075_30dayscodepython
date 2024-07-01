def rekam_presensi():
    absen = []  # List kosong untuk menyimpan nama-nama yang presensi

    while True:
        nama = input("Masukkan nama pekerja yang hadir (atau ketik 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break
        else:
            absen.append(nama)

    # Menampilkan daftar presensi
    print("\nDaftar presensi hari ini:")
    for index, nama in enumerate(absen, start=1):
        print(f"{index}. {nama}")

# Memanggil fungsi untuk merekam presensi
print("=== Program Rekap Absensi ===")
rekam_presensi()
