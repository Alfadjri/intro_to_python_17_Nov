open_file = open("./Contoh_write_text.txt","r")
read_ = open_file.read()
print("Value file Conoth_write_text.txt : ")
print(read_)

# mau menggambil 1 tulisan
# bahasa keren pointer
open_file.seek(0) # ini gunanya untuk mengembalikan komputer agar ke line pertama
print("Ambil 3 karakter di depan dari file Contoh_write_text.txt")
print(open_file.readline(3))

#realines
open_file.seek(0)
print("Ambil 1 baris pertama dari file Contoh_write_text.txt")
for line in open_file.readlines():
    print(line.strip())
    break

open_file.close()
