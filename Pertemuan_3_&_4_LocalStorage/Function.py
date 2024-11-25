#format
# paramter ini syarat yang harus di panggil
# def namaFunctional(paramter)
# function void atau fungsi yang tidak mengeluarkan hasil
def printFormat(nama):
    print(f"Hello ini salah , {nama}".format(nama = nama))

printFormat("Alfajri")
printFormat("Dwi")
printFormat("Fadilah")

def tambah(a , b):
    return a + b

def formatPrint(a,b):
    print("Berapa nilai dari {a} + {b} = {hasil}".format(a=a , b = b , hasil = tambah(a,b)))

a = 10
b = 12

formatPrint(a,b)
a = 11 
b = 10
formatPrint(a,b)
