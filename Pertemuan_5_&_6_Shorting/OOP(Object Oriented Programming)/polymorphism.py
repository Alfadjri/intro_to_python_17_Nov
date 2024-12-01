# case Mobil 

class Mobil:
    def hidupkan_mesin(self):
        return "Mobil menggunakan bensin menyala"

class Mobil_Listrik(Mobil) : 
    def hidupkan_mesin(self):
        return "Mobil listrik Low Batter"
    
# Main program 
def start(Mobil):
    print(Mobil.hidupkan_mesin())

toyota = Mobil()
start(toyota)
tesla = Mobil_Listrik()
start(tesla)