from employee import Employee

class Manger(Employee):
    def __init__(self,nama , umur , pekerjaan , gaji,jumlah_tim):
        super().__init__(nama , umur,pekerjaan,gaji)
        self._jumlah_tim = jumlah_tim
    
    def get_detail(self):
        return (f"Manager : {self._name}, Age : {self.getUmur()},Job : {self._pekerjaan},Gaji : {self._gaji},Jumlah tim : {self._jumlah_tim}")
    def manage(self):
        return f"{self._name} dia bekerja sebagai manager team sebesar {self._jumlah_tim}"
