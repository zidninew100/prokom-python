
def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(f"Mengirim pesan: {message}")
        sent_messages.append(message)


messages = [
    "Jangan menyerah dalam belajar.",
    "Terus berlatih Python.",
    "Kesalahan adalah bagian dari belajar."
]

sent_messages = []

send_messages(messages, sent_messages)

print("\nDaftar pesan awal:")
print(messages)

print("\nDaftar pesan terkirim:")
print(sent_messages)
