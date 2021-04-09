from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jenis_kelamin, jml_penghuni, jml_kamar, kolam="", halaman="", garasi=""):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.jenis_kelamin = jenis_kelamin
        self.kolam = kolam
        self.halaman = halaman
        self.garasi = garasi

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_jenis_kelamin(self):
        return self.jenis_kelamin

    def get_kolam(self):
        return self.kolam

    def get_halaman(self):
        return self.halaman

    def get_garasi(self):
        return self.garasi