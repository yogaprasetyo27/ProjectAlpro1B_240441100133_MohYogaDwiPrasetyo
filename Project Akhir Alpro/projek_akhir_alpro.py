import random

kata = {
    "python": "Bahasa pemrograman",
    "javascript": "Bahasa pemrograman",
    "php": "Bahasa pemrograman",
    "java": "Bahasa pemrograman",
    "css": "Bahasa pemrograman",
    
    "gitar": "Alat musik",
    "kendang": "Alat musik",
    "bas": "Alat musik",
    "drum": "Alat musik",
    "gamelan": "Alat musik",
    "kolintang": "Alat musik",
    
    "semangka": "Nama buah",
    "apel": "Nama buah",
    "mangga": "Nama buah",
    "nanas": "Nama buah",
    "durian": "Nama buah",
    "melon": "Nama buah",
    "pisang": "Nama buah",
    "leci": "Nama buah",
    
    "gajah": "Hewan berkaki 4",
    "kambing": "Hewan berkaki 4",
    "jerapah": "Hewan berkaki 4",
    "serigala": "Hewan berkaki 4",
    "kuda": "Hewan berkaki 4",
    "singa": "Hewan berkaki 4",
    "rusa": "Hewan berkaki 4",
    "kucing": "Hewan berkaki 4",
    
    "pecel": "Makanan Indonesia",
    "rendang": "Makanan Indonesia",
    "kupang": "Makanan Indonesia",
    "soto": "Makanan Indonesia",
    "bakso": "Makanan Indonesia",
    "sate": "Makanan Indonesia",
    
    "melati": "Nama bunga",
    "anggrek": "Nama bunga",
    "raflesia": "Nama bunga",
    "mawar": "Nama bunga",
    "matahari": "Nama bunga",
    
    "komputer": "Alat elektronik",
    "laptop": "Alat elektronik",
    "handphone": "Alat elektronik",
    "radio": "Alat elektronik",
    "televisi": "Alat elektronik",
    "dvd": "Alat elektronik",
    
    "sidoarjo": "Nama kabupaten di Jawa Timur",
    "ngawi": "Nama kabupaten di Jawa Timur",
    "bangkalan": "Nama kabupaten di Jawa Timur",
    "bojonegoro": "Nama kabupaten di Jawa Timur",
    "mojokerto": "Nama kabupaten di Jawa Timur",
    "surabaya": "Nama kabupaten di Jawa Timur",
    "tuban": "Nama kabupaten di Jawa Timur",
    
    "ibrahim": "Nama-nama nabi",
    "muhammad": "Nama-nama nabi",
    "ilyas": "Nama-nama nabi",
    "ismail": "Nama-nama nabi",
    "yusuf": "Nama-nama nabi",
    "yunus": "Nama-nama nabi",
    "harun": "Nama-nama nabi",
    "adam": "Nama-nama nabi",
    "musa": "Nama-nama nabi",
    
    "minotaur": "Nama hero Mobile Legend",
    "lylia": "Nama hero Mobile Legend",
    "johnson": "Nama hero Mobile Legend",
    "gusion": "Nama hero Mobile Legend",
    "miya": "Nama hero Mobile Legend",
    "yuzhong": "Nama hero Mobile Legend",
    "balmond": "Nama hero Mobile Legend",
    "ling": "Nama hero Mobile Legend",
    "vexana": "Nama hero Mobile Legend",
    "lesley": "Nama hero Mobile Legend",
    "nana": "Nama hero Mobile Legend",
}

skor_terakhir = []

def pilih_kata_random(level):
    if level == 1:
        panjang_min, panjang_max = 3, 4
    elif level == 2:
        panjang_min, panjang_max = 5, 7
    elif level == 3:
        panjang_min, panjang_max = 8, 10
    else:
        return None  
    
    kata_terpilih = {
        k: v for k, v in kata.items() if panjang_min <= len(k) <= panjang_max
    }
    
    if kata_terpilih:
        return random.choice(list(kata_terpilih.items()))
    else:
        return None  


def hitung_huruf_benar(kata_tebakan, tebakan):
    huruf_benar = sum(1 for i in range(len(kata_tebakan)) 
                      if i < len(tebakan) and tebakan[i] == kata_tebakan[i])
    return huruf_benar

def tampilkan_status_permainan(status_tebakan, nyawa, skor):
    print("\nStatus permainan:")
    print("Kata saat ini:", " ".join(status_tebakan))
    print(f"Sisa nyawa: {nyawa}")
    print(f"Skor saat ini: {skor}")
    print("=======================================================")

def permainan_tebak_kata():
    nama = input("\nMasukkan nama anda: ")
    print(f"Selamat datang di permainan tebak kata {nama}")

    print("\nPilih tingkat kesulitan:")
    print("1. Mudah (3-4 karakter)")
    print("2. Sedang (5-7 karakter)")
    print("3. Sulit (8-10 karakter)")

    while True:
        pilihan = input("Masukkan nomor pilihan (1/2/3): ")
        if pilihan in ["1", "2", "3"]:
            break
        else:
            print("Input tidak valid!!!")
            
    kata_terpilih = pilih_kata_random(int(pilihan))
    
    if not kata_terpilih:
        print("Pilihan tidak valid.")
        return

    kata_tebakan, petunjuk = kata_terpilih
    nyawa = 3
    skor = 0
    status_tebakan = ["_"] * len(kata_tebakan)

    print("\n=======================================================")
    print("Petunjuk:", petunjuk)
    print("Kata ada:", len(kata_tebakan), "karakter")
    
    while nyawa > 0:
        tampilkan_status_permainan(status_tebakan, nyawa, skor)
        
        tebakan = input("\nMasukkan tebakan anda: ")
        
        konfirmasi = input(f"Yakin dengan jawaban anda '{tebakan}'? Ingin mengubahnya? (y/n): ")
        if konfirmasi == "y":
            tebakan = input("Masukkan kata tebakan baru: ")
        
        if len(tebakan) != len(kata_tebakan):
            print(f"\nPanjang kata harus {len(kata_tebakan)} huruf!")
            continue

        huruf_benar = hitung_huruf_benar(kata_tebakan, tebakan)
        
        for i in range(len(kata_tebakan)):
            if tebakan[i] == kata_tebakan[i]:
                status_tebakan[i] = tebakan[i]
        
        if tebakan == kata_tebakan:
            bonus = len(kata_tebakan) * 10 
            skor += bonus
            print(f"\nSelamat! anda berhasil menebak kata: {kata_tebakan}")
            print(f"Bonus: +{bonus} poin!")
            break
        else:
            nyawa -= 1
            skor -= 10 
            print(f"\nTebakan salah! -10 poin")
            
            if nyawa == 0:
                bonus = huruf_benar * 5  
                print(f"\nPermainan berakhir!")
                print(f"Kata yang benar adalah: {kata_tebakan}")
                print(f"Skor sebelumnya: {skor}")
                print(f"Bonus huruf benar: +{bonus} poin ({huruf_benar} huruf)")
                skor += bonus

    skor_terakhir.append({"nama": nama, "skor": skor})
    print("\nPermainan selesai!")
    print(f"Skor akhir: {skor}")
    print("=======================================================")

def tampil_skor():
    print("\n=======================================================")
    print("Klasemen sementara:")
    if skor_terakhir:
        skor_terakhir.sort(key=lambda x: x["skor"], reverse=True)
        for i, daftar in enumerate(skor_terakhir):
            print(f"{i+1}. {daftar['nama']}: {daftar['skor']} poin")
        print("=======================================================")
    else:
        print("Belum ada skor")

def hapus_data():
    if skor_terakhir:
        print("\n=======================================================")
        print("Daftar skor yang tersedia")
        print("=======================================================")
        for i, daftar in enumerate(skor_terakhir):
            print(f"{i+1}. {daftar['nama']}: {daftar['skor']} point.")
        print("=======================================================")
    else:
        print("\nTidak ada data yang bisa dihapus")
        return
    
    while True:
        print("\nPilih opsi penghapusan:")
        print("1. Hapus data tertentu")
        print("2. Hapus semua data")
        print("3. Kembali ke menu utama")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")
        
        if pilihan == "1":
            nomor = int(input("Masukkan nomor data yang ingin dihapus: "))
            if 1 <= nomor <= len(skor_terakhir):
                data_terhapus = skor_terakhir.pop(nomor - 1)
                print(f"\nData {data_terhapus['nama']} berhasil dihapus!")
            else:
                print("Nomor tidak valid!")
        elif pilihan == "2":
            konfirmasi = input("Anda yakin ingin menghapus semua data? (y/n): ")
            if konfirmasi == 'y':
                skor_terakhir.clear()
                print("\nSemua data berhasil dihapus!")
            else:
                print("Batal menghapus semua data!")
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")

while True:
    print("\nMenu Utama:")
    print("1. Mulai permainan")
    print("2. Tampilkan daftar skor")
    print("3. Hapus data")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        permainan_tebak_kata()
    elif pilihan == "2":
        tampil_skor()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        print("Terima kasih telah bermain!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")