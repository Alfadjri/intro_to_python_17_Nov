siswas = {
    "kelas" : 12,
    "jurusan" : [
        "ipa","ips"
    ] ,
    "nama_ketua" : "udin"
}

# Read semua data
print("Data mentah : {0}".format(siswas))
# read spesifik
print("Kelas : {0}".format(siswas["kelas"]))
print("Jurusan : {0}".format(siswas["jurusan"][1]))
# add atau append
siswas["nilai"] = 10
nilai_siswa = siswas["nilai"] + 13
# update nilai
siswas["nilai"] = nilai_siswa
print("Niliai siswa : {0}".format(siswas["nilai"]))

# di hapus
del siswas["nilai"]
print("Data mentah  : {0}".format(siswas))