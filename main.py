from cryptexpy.encryption import caesar_encrypt, caesar_decrypt
from cryptexpy.hashing import hash_text
from cryptexpy.file_handler import write_to_file, read_from_file

def main():
    print("==== CRYPTEXPY: Cryptography Tool ====")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Hash Text (SHA-256)")
    print("4. Read from File")
    print("5. Write to File")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift key: "))
            encrypted = caesar_encrypt(text, shift)
            print("Encrypted Text:", encrypted)

        elif choice == "2":
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift key: "))
            decrypted = caesar_decrypt(text, shift)
            print("Decrypted Text:", decrypted)

        elif choice == "3":
            text = input("Enter text to hash: ")
            hashed = hash_text(text)
            print("SHA-256 Hash:", hashed)

        elif choice == "4":
            filename = input("Enter filename to read: ")
            content = read_from_file(filename)
            if content:
                print("File Content:\n", content)

        elif choice == "5":
            filename = input("Enter filename to write to: ")
            data = input("Enter data to write: ")
            write_to_file(filename, data)
            print("Data written to", filename)

        elif choice == "0":
            print("Exiting CRYPTEXPY. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

