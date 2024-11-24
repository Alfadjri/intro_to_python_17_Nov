nilai_rapot = 100

# if 
# format
# if (kondisi) :
#   apa yang akan kamu lakukan kalau kondisinya terpenuhi
print("=============if=============")
if (nilai_rapot >= 100):
        print("Selamat kamu lulus dengan nilai yang sempurna")

nilai_rapot = 50
print("============if-else============")
if(nilai_rapot >= 60):
        print("Selamat kamu lulus dalam ujian ini ")
else:
        print("Kamu tidak lulus silahkan lakukan ujian ulang")
# singkatan
# tenery 
# kondisinya cuman untuk nilai sesaat atau kondisi yang singkat
print("============tenery if else============")
pesan = "A" if nilai_rapot >= 60 else "C"
print ("nilai kamu : {0}".format(pesan))

print("============if elif else (if else bersarang atau nesterd)============")
nilai_rapot = 75
if (nilai_rapot >= 90) :
        print("Selamat kamu lulus dengan nilai Semupurna")
elif(nilai_rapot >= 70 and nilai_rapot <= 80) :
        if(nilai_rapot >= 75):
                print("nilai unik hampir tidak lulus")
        else :
            print("Selamat kamu lulus")
else:
        print("Kamu tidak lulus")

# Switch case
print("============Switch case============")
print("Selamat datang di menu")
print("1 . Start")
print("2 . exit")
select = input("Selection => ")
match select:
        case "1" :
                print("Game Start")
        case "2" : 
                print("Game Over")
        case _ :
                print("Input not valid")


