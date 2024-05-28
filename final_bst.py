#class node ini berisi data barang yang akan diinputkan ke dalam binary search tree
#yang terdiri dari nama,harga,stok,sku,left,right
#left dan right ini adalah pointer yang menunjuk ke node lain ke node kiri atau kanan dengan
#menyesuaikan nilai sku dan juga merujuk pada strukdata binary search tree
class Node:
    def __init__(self, sku, nama, harga, stok):
        self.sku = sku
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.left = None
        self.right = None

#fungsi class BinarySearchTree ini sudah sesuai dengan modul yang diberikan
class BinarySearchTree:
    def __init__(self):
        self.root = None 

    #fungsi insert ini berfungsi untuk memasukkan data barang ke dalam binary search tree
    def insert(self, sku, nama, harga, stok):
        #membuat node baru
        new_node = Node(sku, nama, harga, stok)
        #new_node =  Misalnya Node(1234, "Buku", 10000, 10)
        if self.root is None:
            #jika root masih kosong maka node baru akan menjadi root
            self.root = new_node
            #mengembalikan nilai true
            return True
        #membuat variabel temp yang menunjuk ke root
        temp = self.root

        #melakukan perulangan selama true
        while True:
            #jika sku dari node baru sama dengan sku dari temp
            if new_node.sku == temp.sku:
                #maka akan mengembalikan nilai false
                return False
                
                #jika sku dari node baru lebih kecil dari sku dari temp
            if new_node.sku < temp.sku:
                #jika temp.left adalah none
                if temp.left is None:
                    #maka temp.left adalah node baru
                    temp.left = new_node
                    #mengembalikan nilai true
                    return True
                #jika temp.left bukan none
                temp = temp.left

                #jika sku dari node baru lebih besar dari sku dari temp
            else:
                if temp.right is None:
                    #maka temp.right adalah node baru
                    temp.right = new_node
                    return True
                temp = temp.right

    #fungsi contains ini berfungsi untuk mengecek apakah sku yang diinputkan sudah ada di dalam binary search tree
    def contains(self, sku):
        #membuat variabel temp yang menunjuk ke root yang berisi dari self.root root ini adalah node yang pertama kali diinputkan
        temp = self.root

        #melakukan perulangan selama temp tidak none
        while temp is not None:
            #jika sku yang diinputkan sama dengan sku dari temp
            if sku < temp.sku:
                #maka temp adalah temp.left
                temp = temp.left
            #jika sku yang diinputkan lebih besar dari sku dari temp
            elif sku > temp.sku:
                #maka temp adalah temp.right atau temp kanan treenya berada di sebelah kanan untuk BSTnya
                temp = temp.right
            else:
                #mengembalikan nilai temp
                return temp
        return None

    #fungsi restock ini berfungsi untuk menambahkan stok barang yang sudah ada di dalam binary search tree
    def restock(self, sku, jumlah):
        #membuat variabel node yang berisi dari fungsi contains yang berisi sku
        node = self.contains(sku)
        #jika node ada
        if node:
            #maka node.stok adalah node.stok ditambah jumlah
            node.stok += jumlah
            #mengembalikan nilai true dan menampilkan pesan stok barang berhasil ditambahkan
            print(f"Stok barang {node.nama} berhasil ditambahkan. Total stok: {node.stok}")
        else:
            #jika node tidak ada maka akan menampilkan pesan SKU tidak ditemukan
            print("SKU tidak ditemukan.")

    #fungsi display ini berfungsi untuk menampilkan data barang yang ada di dalam binary search tree
    def display(self, node):
        if node:
            #menampilkan data barang yang ada di dalam binary search tree
            self.display(node.left)
            print(f"SKU: {node.sku}, Nama: {node.nama}, Harga: {node.harga}, Stok: {node.stok}")
            self.display(node.right)

# Data Transaksi Konsumen
transaksi_konsumen = []

def lihat_barang_dan_stok():
    print("\n=== Data Barang dan Jumlah Stok ===")
    if bst.root is None:
        print("Belum ada data barang yang diinputkan.")
    else:
        print("Daftar Barang:")
        bst.display(bst.root)

def menu_utama():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Kelola Stok Barang")
        print("2. Kelola Transaksi Konsumen")
        print("3. Lihat Barang dan Jumlah Stok")
        print("0. Exit Program")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            kelola_stok_barang()
        elif pilihan == '2':
            kelola_transaksi_konsumen()
        elif pilihan == '3':
            lihat_barang_dan_stok()
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
    while True:
        try:
            sku = int(input("Masukkan SKU (4 digit angka): "))
            if 1000 <= sku <= 9999:
                break
            else:
                print("SKU harus terdiri dari 4 digit angka.")
        except ValueError:
            print("Input tidak valid. Harap masukkan 4 digit angka.")

    if bst.contains(sku):
        print("SKU sudah ada di BST.")
    else:
        nama = input("Masukkan nama barang: ")
        harga = float(input("Masukkan harga satuan: "))
        stok = int(input("Masukkan jumlah stok: "))
        bst.insert(sku, nama, harga, stok)
        print("Data stok barang berhasil ditambahkan.")

#fungsi restok_barang ini berfungsi untuk menambahkan stok barang yang sudah ada di dalam binary search tree
def restok_barang():
    #jika root adalah none maka akan menampilkan pesan belum ada data barang yang diinputkan
    while True:
        try:
            #membuat variabel sku yang berisi dari inputan sku
            sku = int(input("Masukkan SKU (4 digit angka): "))
            if 1000 <= sku <= 9999:
                break
            else:
                print("SKU harus terdiri dari 4 digit angka.")
        except ValueError:
            print("Input tidak valid. Harap masukkan 4 digit angka.")

    # 1234 , 1235, 1236

    # 1237
    node = bst.contains(sku) # 1237
    if node: # true
        jumlah = int(input("Masukkan jumlah stok yang akan ditambahkan: "))
        bst.restock(sku, jumlah)
    else:
        print("SKU tidak ditemukan. Silakan input data stok barang terlebih dahulu.")

def input_data_transaksi_baru():
    nama_konsumen = input("Masukkan nama konsumen: ")
    while True:
        try:
            sku = int(input("Masukkan SKU barang yang dibeli: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan 4 digit angka.")
            continue
        node = bst.contains(sku)
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

# Main Program
if __name__ == "__main__":
    bst = BinarySearchTree()
    menu_utama()