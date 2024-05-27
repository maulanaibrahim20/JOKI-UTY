import sys

# Data stok barang (dalam bentuk dictionary)
stok_barang = {
    '001': {'nama': 'Produk A', 'stok': 50, 'harga': 10000},
    '002': {'nama': 'Produk B', 'stok': 30, 'harga': 15000},
    '003': {'nama': 'Produk C', 'stok': 20, 'harga': 20000}
}

# Data transaksi konsumen (dalam bentuk list)
transaksi_konsumen = []

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("\n=== Menu Utama ===")
    print("1. Lihat Data Stok Barang")
    print("2. Tambah Stok Barang")
    print("3. Lakukan Transaksi")
    print("4. Lihat Data Transaksi")
    print("5. Keluar")

# Fungsi untuk menampilkan data stok barang
def lihat_data_stok():
    print("\n=== Data Stok Barang ===")
    for kode, barang in stok_barang.items():
        print(f"Kode: {kode}, Nama: {barang['nama']}, Stok: {barang['stok']}, Harga: {barang['harga']}")

# Fungsi untuk menambah stok barang
def tambah_stok():
    kode = input("Masukkan kode barang: ")
    if kode in stok_barang:
        jumlah = int(input("Masukkan jumlah stok yang akan ditambahkan: "))
        stok_barang[kode]['stok'] += jumlah
        print(f"Stok barang {stok_barang[kode]['nama']} berhasil ditambahkan.")
    else:
        print("Kode barang tidak ditemukan.")

# Fungsi untuk melakukan transaksi
def lakukan_transaksi():
    kode = input("Masukkan kode barang: ")
    if kode in stok_barang:
        jumlah = int(input("Masukkan jumlah yang dibeli: "))
        if jumlah <= stok_barang[kode]['stok']:
            total_harga = jumlah * stok_barang[kode]['harga']
            stok_barang[kode]['stok'] -= jumlah
            transaksi = {
                'kode_barang': kode,
                'nama_barang': stok_barang[kode]['nama'],
                'jumlah': jumlah,
                'total_harga': total_harga
            }
            transaksi_konsumen.append(transaksi)
            print(f"Transaksi berhasil. Total harga: {total_harga}")
        else:
            print("Stok barang tidak mencukupi.")
    else:
        print("Kode barang tidak ditemukan.")

# Fungsi untuk melihat data transaksi
def lihat_data_transaksi():
    print("\n=== Data Transaksi Konsumen ===")
    if transaksi_konsumen:
        for transaksi in transaksi_konsumen:
            print(f"Kode Barang: {transaksi['kode_barang']}, Nama Barang: {transaksi['nama_barang']}, Jumlah: {transaksi['jumlah']}, Total Harga: {transaksi['total_harga']}")
    else:
        print("Belum ada transaksi.")

# Fungsi utama
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            lihat_data_stok()
        elif pilihan == '2':
            tambah_stok()
        elif pilihan == '3':
            lakukan_transaksi()
        elif pilihan == '4':
            lihat_data_transaksi()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
