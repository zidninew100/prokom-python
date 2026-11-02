current_users = ["Zidni", "Muhammad", "Ahmad", "Rizky", "Fajar"]

new_users = ["zidni", "Nadia", "Rafi", "MUHAMMAD", "Dimas"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Maaf, username {new_user} sudah digunakan. Silakan pilih nama lain.")
    else:
        print(f"Username {new_user} tersedia!")