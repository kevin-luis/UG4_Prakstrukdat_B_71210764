import json

karyawan = {}
kolega = [{},{}]

kolega[0]["Alamat"] = "Jogja"
kolega[1]["Kolega"] = ["Banu", "Rina"]
karyawan["Caca"] = kolega
print(karyawan) 

n = 2
for i in range(n):
    nama = str(input("Masukkan Nama : "))
    
    alamat = str(input("Masukkan Alamat : "))
    kolega = int(input("Masukkan Jumlah Kolega : "))
    for j in range(1, kolega+1):
        nama_kol = input(f"Masukkan nama kolega ke-{j} : ")

        

# with open ("karyawan.json", "r+") as file:
#     file_data = json.load(file)
#     print(file_data["Andy"])
    
