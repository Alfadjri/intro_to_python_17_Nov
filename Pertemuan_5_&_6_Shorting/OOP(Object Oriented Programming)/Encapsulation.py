#kasus mobil 
class Mobil:
    nama_mobil = "default"
    __ya_semau_saya = "default"
    def __init__(self,nama): # di sini kunci 
        self.nama_mobil = nama
    # set 
    def setMerek(self,merek): # pakai ini untuk merubah
        self.__ya_semau_saya = merek
    # get
    def getMerek(self):
        if(self.__ya_semau_saya.lower() == "default"):
            print("Program salah tidak silahakn set nilai terlebih dahulu")
            exit(1)
        return self.__ya_semau_saya

honda = Mobil("CIVIC TURBO")
print("Saya punya mobil : {nama_mobil}".format(nama_mobil = honda.nama_mobil))
# kasus nya saya mau ganti mereknya 
honda.setMerek("Toyota")
print("Dengan merek : {merek}".format(merek= honda.getMerek()))
