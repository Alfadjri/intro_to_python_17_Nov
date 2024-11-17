#int 
#interger adalah angka bulat 
x = 32767
print("ini contoh bilangan integer : {0}".format(x))
#float atau bouble
#bilangan desimal 
f = 10.5
print("ini contoh nilai desimal : {0}".format(f))
# kompleks
z = 2 + 3j
print("iini contoh tipe data complex : {0}".format(z))

#sqyence type
a = [1,2,3,4] # list : sifatnya tipe data harus sama semua tidak bisa di ubah
print(a)
b = (4,5,6)  # truplet : nilainya tidak bisa di ubah
print(b)
c = range(0,5) # range : nomer urut
print(c)

#Type text
#Strings
nama = "Alfadjri dwi fadhilah"

#Mapping type
profile = { "nama" : "Alfadjri Dwi Fadhilah","age" : 24}
print("Siapakah nama anda : {0}".format(profile["nama"]))

# Set type
f = {1,2,3} #set
print(f)
g = frozenset({4,5,6,7}) #froset
print(g)

# Tipe data kondisi boolean
# boolean cuman ada 2 nilai True dan False
kondisi_badan = True


# binary type
i = 0b01000001
#desimal = int(i)
#char = chr(desimal)
#print(char)
print(chr(int(i))) #ubah dari 0b01000001 => 65  ini di ubah jadi char A-> print A
j = bytearray(a)
print(j)
k = memoryview(j)
print(k)