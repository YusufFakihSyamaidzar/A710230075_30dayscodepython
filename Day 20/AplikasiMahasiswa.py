class AplikasiMahasiswa: # Materi Class
    def __init__(self): # Materi Function
        self.data_mahasiswa = {
            'A710230111': {'nama': 'Allison', 'jurusan': 'PTI', 'semester': 1, 'asal': 'Brazil', 'tgl lahir': '10 Mei 2004'},
            'B710340056': {'nama': 'Bella', 'jurusan': 'Sasta Inggris', 'semester': 3,'asal': 'Madiun', 'tgl lahir': '9 Desember 2003'},
            'C710570001': {'nama': 'Clara', 'jurusan': 'Akuntansi', 'semester': 5,'asal': 'Jakarta', 'tgl lahir': '25 Juni 2002'},
            'D710770029': {'nama': 'Dora', 'jurusan': 'Ilmu Kehutanan', 'semester': 7,'asal': 'Madagascar', 'tgl lahir': '1 Januari 2001'}
        } # Materi Struktur Data (Dictionary)

    def tampilkan_data_mahasiswa(self, nim): 
        if nim in self.data_mahasiswa: # Materi Percabangan 
            mahasiswa = self.data_mahasiswa[nim]
            print(f"Data Mahasiswa NIM {nim}:")
            print(f"Nama          :{mahasiswa['nama']}")
            print(f"Jurusan       :{mahasiswa['jurusan']}")
            print(f"Tanggal Lahir :{mahasiswa['tgl lahir']}")
            print(f"Asal          :{mahasiswa['asal']}")
            print(f"Semester      :{mahasiswa['semester']}")
        else:
            print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    def jalankan_aplikasi(self):
        while True: # Materi Perulangan
            print("\nMenu Aplikasi Mahasiswa:")
            print("1. Cari Data Mahasiswa")
            print("2. Keluar")

            pilihan = input("Masukkan pilihan (1/2): ")

            if pilihan == '1':
                nim_input = input("Masukkan NIM Mahasiswa: ").upper()
                self.tampilkan_data_mahasiswa(nim_input)
            elif pilihan == '2':
                print("Terima kasih, telah menggunakan aplikasi.")
                break
            else:
                print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")

aplikasi = AplikasiMahasiswa()
aplikasi.jalankan_aplikasi()
