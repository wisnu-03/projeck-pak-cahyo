# Program Data Perpustakaan

def main_menu():
    print("\n===== Sistem Data Perpustakaan =====")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Perbarui Buku")
    print("4. Hapus Buku")
    print("5. Keluar")

# Inisialisasi database buku (sebagai list sederhana)
buku_list = []

def tambah_buku():
    print("\n--- Tambah Buku ---")
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahun = input("Masukkan tahun terbit: ")

    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun
    }
    buku_list.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def lihat_buku():
    print("\n--- Daftar Buku ---")
    if len(buku_list) == 0:
        print("Tidak ada buku dalam perpustakaan.")
    else:
        for idx, buku in enumerate(buku_list):
            print(f"{idx + 1}. {buku['judul']} | {buku['penulis']} | {buku['tahun']}")

def perbarui_buku():
    print("\n--- Perbarui Buku ---")
    lihat_buku()
    if len(buku_list) == 0:
        return

    try:
        index = int(input("Masukkan nomor buku yang ingin diperbarui: ")) - 1
        if 0 <= index < len(buku_list):
            print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")
            judul_baru = input("Judul baru: ")
            penulis_baru = input("Penulis baru: ")
            tahun_baru = input("Tahun terbit baru: ")

            if judul_baru:
                buku_list[index]["judul"] = judul_baru
            if penulis_baru:
                buku_list[index]["penulis"] = penulis_baru
            if tahun_baru:
                buku_list[index]["tahun"] = tahun_baru

            print("Data buku berhasil diperbarui!")
        else:
            print("Nomor buku tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def hapus_buku():
    print("\n--- Hapus Buku ---")
    lihat_buku()
    if len(buku_list) == 0:
        return

    try:
        index = int(input("Masukkan nomor buku yang ingin dihapus: ")) - 1
        if 0 <= index < len(buku_list):
            buku = buku_list.pop(index)
            print(f"Buku '{buku['judul']}' berhasil dihapus!")
        else:
            print("Nomor buku tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def main():
    while True:
        main_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            lihat_buku()
        elif pilihan == "3":
            perbarui_buku()
        elif pilihan == "4":
            hapus_buku()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
