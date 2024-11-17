x = 3
y = 2
# Penjumlahan
hasil = x + y 
print("hasil penjumlahan dari {x} + {y} = {hasil}".format(x = x , y = y , hasil = hasil))
# pengurangan
hasil = x - y 
print("hasil pengurangan dari {x} - {y} = {hasil}".format(x = x , y = y , hasil = hasil))
# perkalian
hasil = x * y
print("hasil perkalian dari {x} x {y} = {hasil}".format(x = x , y = y , hasil = hasil))
# pembagian
hasil = x / y
hasil_conversi_ke_integer = int(x/y)
print("hasil pembagian dari {x} / {y} = {hasil}".format(x = x , y = y , hasil = hasil))
#modulus
hasil = x % y
print("hasil pembagian dari {x} % {y} = {hasil}".format(x = x , y = y , hasil = hasil))
#perpangkatan
hasil = x ** y
print("hasil pangkat dari {x}^{y} = {hasil}".format(x = x , y = y , hasil = hasil))

# cara menyingkat penjumlahan atau pengurangan
# increment
z = 0
print("Hasil sebelum di tambahakan : {0}".format(z))
# z = z + 3 (old version)
# z++
z+=3 # z = z + 3 => z = 0 + 3
print("Hasil z setelah di tanbahkan : {0}".format(z))
z-=1 # z = z - 1 => z = 3 - 1 
print("Hasil z setelah di kurangkan : {0}".format(z))