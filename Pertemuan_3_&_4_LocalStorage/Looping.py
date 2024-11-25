# While
# di mana di check terlebih dahulu baru di jalankan
# format
#  while(kondisi):
#      apa yang ulang

count = 100 
while( count <= 100) :
    print("index value ke-{0} : Love you ".format(count))
    count += 1

# for 
# range(1,100) artinya buatkan saya angka dari 1 sampai 100
# for varibale_row in banyakData:
# perintah yang akan di ulang
for i in range(1,101):
    print("Range index : {0}".format(i))

# for untuk list
buahs = ["appel","pisang","semangka"]
for value in buahs:
    print("Buah yang ada : {0}".format(value))


# break
# teknik untuk menghentikan nilai
bilangan = 1
while(bilangan <= 100):
    if bilangan % 2 == 0 :
        bilangan += 1
        continue # teknik untuk melanjutkan loop atau keluar dari kondisi tampa memberhentikan
    print(bilangan)
    bilangan += 1

    if bilangan > 40 :
        break # memberhentikan loop secara paksa
    
    

