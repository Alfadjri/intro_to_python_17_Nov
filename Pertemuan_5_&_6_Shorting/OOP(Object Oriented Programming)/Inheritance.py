# case pada keluarga

class Ibu:
    panggilan = "ini punya ibu "
    # def __init__(self,_panggilan = "default"):
    #     self.panggilan = _panggilan

    def memanggil(self):
        print("Iya , Ada apa ? ")
    
    def setSifat(self,sifat):
        self.__sifat = sifat
    
    def getSifat(self):
        return self.__sifat

class Anak(Ibu): #inheritance atau mewariskan
    def suruh(self):
        print("Nanti dulu lah !!!")


# real case
sekolah = Anak()
sekolah.panggilan = "budi"
print("Siapa nama anak ini : {nama_anak}".format(nama_anak = sekolah.panggilan))
sekolah.memanggil()
sekolah.setSifat("anak baik !")
print("Sifat dari budi : {sifat} ".format(sifat = sekolah.getSifat()))
print("Apakh anak bisa di suruh : ")
sekolah.suruh()
