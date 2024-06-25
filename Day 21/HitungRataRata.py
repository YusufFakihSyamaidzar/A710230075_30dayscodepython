def hitung_rata_rata(data_list):
    total = sum(data_list)
    rata_rata = total / len(data_list)
    return rata_rata

# Input angka
input_list = input('Masukkan beberapa Angka dipisah spasi :')
data_list = input_list.split()
data_list = [int(x) for x in data_list]
print(data_list)

result = hitung_rata_rata(data_list) #input yang benar adalah list
print(result)