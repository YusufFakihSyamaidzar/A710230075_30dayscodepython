import os

# Fungsi untuk input data baru
def input_data():
    print("Masukkan data baru:")
    nik = input("NIK: ")
    no_kk = input("No KK: ")
    nama = input("Nama: ")
    tempat_lahir = input("Tempat Lahir: ")
    tanggal_lahir = input("Tanggal Lahir (format: YYYY-MM-DD): ")
    alamat = input("Alamat: ")
    
    data = {
        'NIK': nik,
        'No KK': no_kk,
        'Nama': nama,
        'Tempat Lahir': tempat_lahir,
        'Tanggal Lahir': tanggal_lahir,
        'Alamat': alamat
    }
    return data

# Fungsi untuk menyimpan data ke dalam file
def simpan_data(data):
    with open('data_kartu_keluarga.txt', 'a') as file:
        file.write(str(data) + '\n')
    print("Data berhasil disimpan.\n")

# Fungsi untuk menampilkan semua data yang tersimpan
def tampilkan_data():
    if not os.path.exists('data_kartu_keluarga.txt'):
        print("Belum ada data yang tersimpan.")
        return
    
    print("Daftar Data Kartu Keluarga:")
    with open('data_kartu_keluarga.txt', 'r') as file:
        for line in file:
            print(eval(line))  # Menggunakan eval untuk membaca dictionary dari string
            
    print()

# Fungsi utama aplikasi
def main():
    while True:
        print("===== APLIKASI KARTU KELUARGA =====")
        print("1. Input Data Baru")
        print("2. Tampilkan Data")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")
        
        if pilihan == '1':
            data_baru = input_data()
            simpan_data(data_baru)
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.\n")

if __name__ == "__main__":
    main()
