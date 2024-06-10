# Input tahun kelahiran penumpang
tahun_lahir = int(input("Masukkan tahun kelahiran penumpang: "))
tahun_sekarang = 2024

# Hitung usia penumpang
usia = tahun_sekarang - tahun_lahir

# Input harga tiket kereta api
harga_tiket = int(input("Masukkan harga tiket kereta api: "))

# Tentukan diskon berdasarkan usia
if usia >= 0 and usia <= 4:
    diskon = 1.0  # Diskon 100%
elif usia >= 5 and usia <= 11:
    diskon = 0.5  # Diskon 50%
else:
    diskon = 0.0  # Tidak ada diskon

# Hitung harga setelah diskon
harga_setelah_diskon = harga_tiket * (1 - diskon)

# Tampilkan hasil
print(f"Usia penumpang: {usia} tahun")
print("Diskon:", int(diskon * 100), "%")
print("Harga tiket setelah diskon: Rp.", int(harga_setelah_diskon))