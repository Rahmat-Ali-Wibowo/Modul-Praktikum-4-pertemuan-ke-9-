# Program Mengelola Data Mahasiswa

## Deskripsi
Program ini memungkinkan pengguna untuk menambahkan data mahasiswa secara berulang kali dan menghitung nilai akhir berdasarkan nilai tugas, UTS, dan UAS. Program akan menampilkan daftar data mahasiswa setelah pengguna memutuskan untuk berhenti menambah data.

## Flowchart
```plaintext
+----------------------------------------------------------+
| Mulai                                                     |
+----------------------------------------------------------+
          |
          v
+-------------------+                      +----------------------+
| Buat list kosong  |                      | Menginput nama       |
| data_mahasiswa    |                      | mahasiswa            |
+-------------------+                      +----------------------+
          |                                            |
          v                                            v
+-------------------+                      +----------------------+
| Meminta input     |                      | Menginput nilai      |
| dari pengguna:    +----------------------> tugas, UTS, UAS     |
| Nama, Tugas, UTS, |                      +----------------------+
| dan UAS           |                                      |
+-------------------+                                      v
          |                                 +------------------------------+
          v                                 | Hitung nilai akhir           |
+-------------------+                      +-------------------------------+
| Hitung nilai      +--------------------->| Nilai Akhir = 0.3*Tugas +     |
| akhir             |                      | 0.35*UTS + 0.35*UAS           |
|                   |                      +-------------------------------+
          |                                           |
          v                                           v
+-------------------+                      +-------------------------------+
| Tambahkan data ke |                      | Tambah data lagi?             |
| list              +--------------------->| (y/t)?                        |
| data_mahasiswa    |                      +-------------------------------+
+-------------------+                                      |
          |                                                |
          v                                                v
+-------------------+                      +-------------------------------+
| Apakah menambah   +--------------------->| Jika 't', tampilkan daftar    |
| data lagi (y/t)?  |                      | data mahasiswa                |
| Ya (y)/Tidak (t)? |                      +-------------------------------+
+-------------------+
          |
          v
+-------------------+
| Tampilkan daftar  |
| data mahasiswa    |
+-------------------+
          |
          v
+----------------------------------------------------------+
| Selesai                                                  |
+----------------------------------------------------------+
