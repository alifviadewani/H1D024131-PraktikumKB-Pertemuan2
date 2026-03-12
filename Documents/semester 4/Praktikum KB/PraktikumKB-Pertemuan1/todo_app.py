import random
import datetime

todo_list = []

def tambah_tugas():
    tugas = input("Masukkan nama tugas: ")
    
    id_tugas = random.randint(100,999)
    waktu = datetime.datetime.now()

    data = {
        "id": id_tugas,
        "tugas": tugas,
        "waktu": waktu.strftime("%d-%m-%Y %H:%M")
    }

    todo_list.append(data)

    print("Tugas berhasil ditambahkan!")

def lihat_tugas():
    if len(todo_list) == 0:
        print("Belum ada tugas")
    else:
        print("\nDaftar Tugas")
        for tugas in todo_list:
            print(f"ID: {tugas['id']} | {tugas['tugas']} | {tugas['waktu']}")

def hapus_tugas():
    id_hapus = int(input("Masukkan ID tugas yang ingin dihapus: "))

    for tugas in todo_list:
        if tugas["id"] == id_hapus:
            todo_list.remove(tugas)
            print("Tugas berhasil dihapus")
            return

    print("ID tidak ditemukan")

while True:

    print("\n===== MENU =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        hapus_tugas()

    elif pilihan == "4":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")