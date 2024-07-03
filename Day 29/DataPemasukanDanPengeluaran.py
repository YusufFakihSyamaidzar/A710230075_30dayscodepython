def input_data():
    data = {}
    while True:
        bulan_tahun = input("Masukkan bulan dan tahun (format: MM-YYYY) atau ketik 'selesai' untuk mengakhiri: ")
        if bulan_tahun.lower() == 'selesai':
            break
        else:
            while True:
                try:
                    pemasukan = float(input(f"Masukkan pemasukan untuk bulan {bulan_tahun}: "))
                    pengeluaran = float(input(f"Masukkan pengeluaran untuk bulan {bulan_tahun}: "))
                    break
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")
            data[bulan_tahun] = {
                'pemasukan': pemasukan,
                'pengeluaran': pengeluaran
            }
    return data

def bandingkan_data(data):
    total_pemasukan = 0
    total_pengeluaran = 0
    
    for bulan_tahun, detail in data.items():
        total_pemasukan += detail['pemasukan']
        total_pengeluaran += detail['pengeluaran']
    
    print("\nRincian data:")
    for bulan_tahun, detail in data.items():
        print(f"Bulan {bulan_tahun}: Pemasukan = {detail['pemasukan']}, Pengeluaran = {detail['pengeluaran']}")
    
    print("\nTotal Pemasukan:", total_pemasukan)
    print("Total Pengeluaran:", total_pengeluaran)
    print("Selisih (Pemasukan - Pengeluaran):", total_pemasukan - total_pengeluaran)

def main():
    print("=== Aplikasi Pencatatan Pemasukan dan Pengeluaran Perusahaan ===")
    data = input_data()
    bandingkan_data(data)

if __name__ == "__main__":
    main()
