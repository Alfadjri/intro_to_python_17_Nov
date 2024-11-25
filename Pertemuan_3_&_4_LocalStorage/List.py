# misal 
# puya data makanan
# nisialisasi
makanan = ["nasi","ikan","ayam","sayur","buah","ciki"]

# read
print("isi Data list : {0}".format(makanan))

# read spesifik
# vairable[posisiAtauIndexData]
print("isi dari index ke 3 : {0}".format(makanan[3]))

# update
# variabel[posisiAtauIndexData] = valueYangmaudiIsi
makanan[-1] = "Jeli"
print("isi Data list : {0}".format(makanan))

# append atau insert atau menambahkan data atau tambah data create 
makanan.append("ciki")
makanan.append("bubur")
print("isi Data list : {0}".format(makanan))
# delete
makanan.remove("ciki")
print("isi Data list : {0}".format(makanan))

makanan2 = ["nasi padang" , "nasi lemak"]
makanan_baru = makanan + makanan2
print("isi Data list : {0}".format(makanan_baru))
