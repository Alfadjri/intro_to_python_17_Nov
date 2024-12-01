from abc import ABC , abstractclassmethod

class Kendaraan(ABC):
    @abstractclassmethod
    def menyalakn_mesin(self):
        pass


class Mobil(Kendaraan):
    def menyalakn_mesin(self):
        return "Start"
class Motor(Kendaraan):
    def menyalakn_mesin(self):
        return "Motor Mogok"
    
# kendaraan = Kendaraan()
# print(kendaraan.menyalakn_mesin())
motor = Motor()
print(motor.menyalakn_mesin())
