def encryptVigenere(password, key):
    encrypted_password = ""
    key_length = len(key)
    for i in range(len(password)):
        char = password[i]
        if char.isalpha():
            # Determine the shift value based on the key
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                encrypted_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            encrypted_password += encrypted_char
        else:
            encrypted_password += char
    return encrypted_password


def decryptVigenere(encryptedPassword, key):
    decrypted_password = ""
    key_length = len(key)
    for i in range(len(encryptedPassword)):
        char = encryptedPassword[i]
        if char.isalpha():
            # Determine the shift value based on the key
            shift = ord(key[i % key_length].upper()) - ord('A')
            if char.isupper():
                decrypted_char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            decrypted_password += decrypted_char
        else:
            decrypted_password += char
    return decrypted_password


# Contoh penggunaan
password = "Secret123"
key = "KEY"
encrypted_password = encryptVigenere(password, key)
print(f"Password setelah dienkripsi: {encrypted_password}")

decrypted_password = decryptVigenere(encrypted_password, key)
print(f"Password setelah didekripsi: {decrypted_password}")
