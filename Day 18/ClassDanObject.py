class Orang:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur}")

class Mahasiswa(Orang):
    def __init__(self,nama,umur,universitas):
        super().__init__(nama,umur)
        self.universitas = universitas

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kuliah di {self.universitas}")
        
class Pekerja(Orang):
    def __init__(self,nama,umur,tempatkerja):
        super().__init__(nama,umur)
        self.tempatkerja = tempatkerja

    def kenalan(self):
        print(f"Halo, namaku {self.nama}, umurku {self.umur} dan aku kerja di {self.tempatkerja}")

orang = Orang('Yuu', 18)
orang.kenalan()

mahasiswa = Mahasiswa('Yuu', 18,'UMS')
mahasiswa.kenalan()

pekerja = Pekerja('Yuu', 18,'Perusahaan')
pekerja.kenalan()
