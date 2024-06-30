class Tiket:
    def __init__(self, jumlah_tiket):
        self.jumlah_tiket = jumlah_tiket
        self.harga_per_tiket = 0

    def hitung_total_harga(self):
        total_harga = self.jumlah_tiket * self.harga_per_tiket
        return total_harga

class TiketBiasa(Tiket):
    def __init__(self, jumlah_tiket):
        super().__init__(jumlah_tiket)
        self.harga_per_tiket = 30000

class TiketVIP(Tiket):
    def __init__(self, jumlah_tiket):
        super().__init__(jumlah_tiket)
        self.harga_per_tiket = 55000

class TiketGold(Tiket):
    def __init__(self, jumlah_tiket):
        super().__init__(jumlah_tiket)
        self.harga_per_tiket = 80000

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ").upper()
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jenis_tiket == 'BIASA':
        tiket = TiketBiasa(jumlah_tiket)
    elif jenis_tiket == 'VIP':
        tiket = TiketVIP(jumlah_tiket)
    elif jenis_tiket == 'GOLD':
        tiket = TiketGold(jumlah_tiket)
    else:
        print("Jenis tiket tidak valid!")
        return

    total_harga = tiket.hitung_total_harga()
    print("Total Harga Tiket: Rp", total_harga)

main()
    