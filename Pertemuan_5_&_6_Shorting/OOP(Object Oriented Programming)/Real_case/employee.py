from person import Person

class Employee(Person):
    def __init__(self, nama , umur , pekerjaan , gaji):
        super().__init__(nama,umur)
        self._pekerjaan = pekerjaan
        self._gaji = gaji
    def get_detail(self):
        return f"Employee : {self._name}, Age : {self.getUmur()},Job : {self._pekerjaan},Gaji : {self._gaji}"
    def work(self):
        return f"{self._name} dia berkerja sebagai {self._pekerjaan}"