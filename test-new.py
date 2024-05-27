class Node:
    def __init__(self, sku, nama, harga, stok):
        self.sku = sku
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, sku, nama, harga, stok):
        if self.root is None:
            self.root = Node(sku, nama, harga, stok)
        else:
            self._insert(self.root, sku, nama, harga, stok)

    def _insert(self, current_node, sku, nama, harga, stok):
        if sku < current_node.sku:
            if current_node.left is None:
                current_node.left = Node(sku, nama, harga, stok)
            else:
                self._insert(current_node.left, sku, nama, harga, stok)
        elif sku > current_node.sku:
            if current_node.right is None:
                current_node.right = Node(sku, nama, harga, stok)
            else:
                self._insert(current_node.right, sku, nama, harga, stok)
        else:
            print("SKU sudah ada di BST.")

    def search(self, sku):
        return self._search(self.root, sku)

    def _search(self, current_node, sku):
        if current_node is None:
            return None
        elif current_node.sku == sku:
            return current_node
        elif sku < current_node.sku:
            return self._search(current_node.left, sku)
        else:
            return self._search(current_node.right, sku)

    def restock(self, sku, jumlah):
        node = self.search(sku)
        if node:
            node.stok += jumlah
            print(f"Stok barang {node.nama} berhasil ditambahkan. Total stok: {node.stok}")
        else:
            print("SKU tidak ditemukan.")

    def display(self, node):
        if node:
            self.display(node.left)
            print(f"SKU: {node.sku}, Nama: {node.nama}, Harga: {node.harga}, Stok: {node.stok}")
            self.display(node.right)

# Data Transaksi Konsumen
transaksi_konsumen = []

def menu_utama():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Kelola Stok Barang")
        print("2. Kelola Transaksi Konsumen")
        print("0. Exit Program")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            kelola_stok_barang()
        elif pilihan == '2':
            kelola_transaksi_konsumen()
        elif pilihan == '0':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def kelola_stok_barang():
    while True:
        print("\n=== Kelola Stok Barang ===")
        print("1. Input Data Stok Barang")
        print("2. Restok Barang")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            input_data_stok_barang()
        elif pilihan == '2':
            restok_barang()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def kelola_transaksi_konsumen():
    while True:
        print("\n=== Kelola Transaksi Konsumen ===")
        print("1. Input Data Transaksi Baru")
        print("2. Lihat Data Seluruh Transaksi Konsumen")
        print("3. Lihat Data Transaksi Berdasarkan Subtotal")
        print("0. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            input_data_transaksi_baru()
        elif pilihan == '2':
            lihat_data_seluruh_transaksi()
        elif pilihan == '3':
            lihat_data_transaksi_berdasarkan_subtotal()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def input_data_stok_barang():
    sku = input("Masukkan SKU (4 digit angka): ")
    if bst.search(sku):
        print("SKU sudah ada di BST.")
    else:
        nama = input("Masukkan nama barang: ")
        harga = float(input("Masukkan harga satuan: "))
        stok = int(input("Masukkan jumlah stok: "))
        bst.insert(sku, nama, harga, stok)
        print("Data stok barang berhasil ditambahkan.")

def restok_barang():
    sku = input("Masukkan SKU (4 digit angka): ")
    if bst.search(sku):
        jumlah = int(input("Masukkan jumlah stok yang akan ditambahkan: "))
        bst.restock(sku, jumlah)
    else:
        print("SKU tidak ditemukan. Silakan input data stok barang terlebih dahulu.")

def input_data_transaksi_baru():
    nama_konsumen = input("Masukkan nama konsumen: ")
    while True:
        sku = input("Masukkan SKU barang yang dibeli: ")
        node = bst.search(sku)
        if node:
            jumlah_beli = int(input("Masukkan jumlah yang dibeli: "))
            if jumlah_beli <= node.stok:
                subtotal = jumlah_beli * node.harga
                node.stok -= jumlah_beli
                transaksi = {
                    'nama_konsumen': nama_konsumen,
                    'sku': sku,
                    'jumlah_beli': jumlah_beli,
                    'subtotal': subtotal
                }
                transaksi_konsumen.append(transaksi)
                print("Data Transaksi Konsumen Berhasil Diinputkan")
            else:
                print("Jumlah Stok No.SKU yang Anda beli tidak mencukupi")
                lanjutkan = input("Apakah ingin melanjutkan transaksi (Y/N)? ").upper()
                if lanjutkan == 'N':
                    break
        else:
            print("No. SKU yang diinputkan belum terdaftar")
            lanjutkan = input("Apakah ingin melanjutkan transaksi (Y/N)? ").upper()
            if lanjutkan == 'N':
                break

        tambah = input("Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)? ").upper()
        if tambah == 'N':
            break

def lihat_data_seluruh_transaksi():
    print("\n=== Data Seluruh Transaksi Konsumen ===")
    if transaksi_konsumen:
        for transaksi in transaksi_konsumen:
            print(f"Nama Konsumen: {transaksi['nama_konsumen']}, SKU: {transaksi['sku']}, Jumlah Beli: {transaksi['jumlah_beli']}, Subtotal: {transaksi['subtotal']}")
    else:
        print("Belum ada transaksi.")

def lihat_data_transaksi_berdasarkan_subtotal():
    if not transaksi_konsumen:
        print("Belum ada transaksi.")
        return

    sorted_transaksi = sorted(transaksi_konsumen, key=lambda x: x['subtotal'], reverse=True)
    print("\n=== Data Transaksi Berdasarkan Subtotal ===")
    for transaksi in sorted_transaksi:
        print(f"Nama Konsumen: {transaksi['nama_konsumen']}, SKU: {transaksi['sku']}, Jumlah Beli: {transaksi['jumlah_beli']}, Subtotal: {transaksi['subtotal']}")

if __name__ == "__main__":
    bst = BST()
    menu_utama()
