mahasiswa = {
    'nama': 'Andika',
    'umur': 21}

# Mengubah umur
mahasiswa['umur'] = 19

# Menambahkan alamat dan angkatan
mahasiswa['alamat'] = 'Sragen'
mahasiswa['angkatan'] = 2020

# Menampilkan data mahasiswa
print(mahasiswa)

# Menghapus dan menampilkan angkatan
print(mahasiswa.pop('angkatan'))

# Menampilkan data mahasiswa setelah penghapusan
print(mahasiswa)

# Memeriksa keberadaan 'nama' di dalam dictionary
print('nama' in mahasiswa)

# Menampilkan jumlah elemen dalam dictionary
print(len(mahasiswa))

# Menampilkan kunci-kunci dalam dictionary yang diurutkan
print(sorted(mahasiswa))

# Menghapus semua elemen dalam dictionary
mahasiswa.clear()

# Menampilkan dictionary setelah dikosongkan
print(mahasiswa)
