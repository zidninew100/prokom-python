usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Halo admin, apakah kamu ingin melihat laporan hari ini?")
        else:
            print(f"Halo {username}, terima kasih sudah login kembali!")
else:
    print("Kita perlu mencari pengguna baru!")