# Buat daftar dengan 5 elemen
A = [10, 20, 30, 40, 50]

# Akses daftar
print("Elemen ke-3:", A[2])  # Tampilkan elemen ke-3
print("Elemen ke-2 sampai ke-4:", A[1:4])  # Ambil nilai elemen ke-2 sampai elemen ke-4
print("Elemen terakhir:", A[-1])  # Ambil elemen terakhir

# Ubah elemen daftar
A[3] = 100  # Ubah elemen ke-4 dengan nilai lain
print("Daftar setelah mengubah elemen ke-4:", A)

A[3:] = [100, 200]  # Ubah elemen ke-4 sampai dengan elemen terakhir
print("Daftar setelah mengubah elemen ke-4 sampai terakhir:", A)

# Tambah elemen daftar
B = A[:2]  # Ambil 2 bagian dari daftar pertama (A) dan jadikan daftar kedua (B)
print("Daftar B:", B)

B.append("hello")  # Tambah daftar B dengan nilai string
print("Daftar B setelah menambah string:", B)

B.extend([60, 70, 80])  # Tambah daftar B dengan 3 nilai
print("Daftar B setelah menambah 3 nilai:", B)

combined_list = B + A  # Gabungkan daftar B dengan daftar A
print("Gabungan daftar B dan A:", combined_list)
