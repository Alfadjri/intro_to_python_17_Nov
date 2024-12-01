#kasus
# kita amati hewan 

class Hewan : # hewan itu nama dari kelass
    nama_hewan = "default" # nama_hewa ini di sebut object
    jenis_hewan = "default"
    _umur_hewan = 10 # property umur_hewan sifatnya private 
    # construktor 
    def __init__(self,nama,jenis):
        self.nama_hewan = nama
        self.jenis_hewan = jenis

    def makan(self):
        print("Hewan sedang makan !!!")


# Cara manggil 
kucing = Hewan("tom","anggora")
# kucing = Hewan() # ini tampa konstruktor
# varibel 
print("nama kucing {nama}".format(nama= kucing.nama_hewan))
print("jenis kucing {jenis}".format(jenis = kucing.jenis_hewan))
print("Umur kucing {umur}".format(umur = kucing._umur_hewan))
# untuk manggil fungsi atau method
print("kucing sengan apa ?")
kucing.makan()


