def hitung_nilai_akhir(tugas, uts, uas):
    return 0.3 * tugas + 0.35 * uts + 0.35 * uas

data_mahasiswa = []

while True:
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa.append({
        'nama': nama,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    })
    
    tambah_data = input("Apakah Anda ingin menambah data lagi? (y/t): ").lower()
    if tambah_data == 't':
        break

print("\nDaftar Data Mahasiswa:")
for mahasiswa in data_mahasiswa:
    print(f"Nama: {mahasiswa['nama']}, Tugas: {mahasiswa['tugas']}, UTS: {mahasiswa['uts']}, UAS: {mahasiswa['uas']}, Nilai Akhir: {mahasiswa['nilai_akhir']:.2f}")
