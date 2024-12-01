import random

def random_number_generate(banyak_data):
    list_data = []
    for i in range(banyak_data):
        nilai_acak = random.randint(1,100)
        list_data.append(nilai_acak)
    return list_data

# bubble short
def short_bubble(data):
    n = len(data)

    # logic 
    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] > data[j+1]:
                # temp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = temp
                data[j],data[j+1] = data[j+1], data[j]

def selection_short(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if data[j] < data[min_index]:
                min_index = j
        
        data[i],data[min_index] = data[min_index], data[i]
        

banyak_data = int(input("Banyak data yang akan di shorting : "))
list_data = random_number_generate(banyak_data)
print("List data yang belum di urutkan : ")
print(list_data)
print("List data setelah di urutkan :")
# short_bubble(list_data)
selection_short(list_data)
print(list_data)