from cryptexpy.ciphers import caesar_cipher, vigenere_cipher
from cryptexpy.hashing import hash_text
from cryptexpy.file_handler import write_to_file, read_from_file


def main():
    while True:
        print("\n==== CRYPTEXPY: Cryptography Tool ====")
        print("1. Encrypt with Caesar Cipher")
        print("2. Decrypt with Caesar Cipher")
        print("3. Encrypt with Vigenère Cipher")
        print("4. Decrypt with Vigenère Cipher")
        print("5. Hash Text (SHA-256)")
        print("6. Read from File")
        print("7. Write to File")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            text = input("Enter text to encrypt (Caesar): ")
            key = int(input("Enter shift key: "))
            result = caesar_cipher(text, key, mode='encrypt')
            print("Encrypted Text:", result)

        elif choice == "2":
            text = input("Enter text to decrypt (Caesar): ")
            key = int(input("Enter shift key: "))
            result = caesar_cipher(text, key, mode='decrypt')
            print("Decrypted Text:", result)

        elif choice == "3":
            text = input("Enter text to encrypt (Vigenère): ")
            keyword = input("Enter keyword: ")
            result = vigenere_cipher(text, keyword, mode='encrypt')
            print("Encrypted Text:", result)

        elif choice == "4":
            text = input("Enter text to decrypt (Vigenère): ")
            keyword = input("Enter keyword: ")
            result = vigenere_cipher(text, keyword, mode='decrypt')
            print("Decrypted Text:", result)

        elif choice == "5":
            text = input("Enter text to hash: ")
            hashed = hash_text(text)
            print("SHA-256 Hash:", hashed)

        elif choice == "6":
            filename = input("Enter filename to read from: ")
            content = read_from_file(filename)
            if content:
                print("File Content:\n", content)

        elif choice == "7":
            filename = input("Enter filename to write to: ")
            data = input("Enter text to write: ")
            write_to_file(filename, data)
            print(f"Data written to '{filename}' successfully.")

        elif choice == "0":
            print("Exiting CRYPTEXPY. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
