# Membuat Input Usia
usia = int(input("Masukkan usia Anda: "))
darah = int(input("Masukkan tekanan darah Anda: "))

# Membuat percabangan kategori status kesehatan
if usia >= 60 and darah > 140:
    print("Status Kesehatan: Tinggi")
elif usia >= 60 and darah <= 140:
    print("Status Kesehatan: Normal")
elif usia < 60 and darah > 130:
    print("Status Kesehatan: Tinggi")
elif usia < 60 and darah <= 130:
    print("Status Kesehatan: Normal")
else: 
    print("Status Kesehatan Normal")









