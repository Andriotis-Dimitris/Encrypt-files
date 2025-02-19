# Encryption Script

## Overview
This repository contains a simple file encryption and decryption script using the `cryptography` library in Python. The scripts are designed to encrypt all files in the current directory (excluding certain files) and securely store the encryption key.

## Files
- **`ransomware.py`**: This script encrypts all non-excluded files in the directory using a randomly generated encryption key.
- **`decrypt.py`**: This script (intended to be implemented) will decrypt the encrypted files using the stored key.
- **`thekey.key`**: The generated key file used for encryption and decryption.

## How It Works
### Encryption (`ransomware.py`):
1. Identifies all non-excluded files in the current directory.
2. Generates a secure encryption key and saves it to `thekey.key`.
3. Encrypts the identified files and overwrites them with the encrypted content.
4. Displays a message indicating successful encryption.

### Decryption (`decrypt.py`):
1. Reads the stored encryption key from `thekey.key`.
2. Identifies all encrypted files.
3. Decrypts the files using the stored key.
4. Restores the original content.

## Dependencies
Ensure you have the required dependencies installed:
```sh
pip3 install cryptography
```

## Usage
### Encrypt Files:
Run the encryption script:
```sh
python3 ransomware.py
```
This will encrypt all non-excluded files in the directory.

### Decrypt Files (To be implemented):
Run the decryption script:
```sh
python3 decrypt.py
```
Ensure that `thekey.key` is present in the directory.

## Disclaimer
This project is for educational and testing purposes only. **Do not use this for malicious activities.** The purpose is to demonstrate file encryption concepts.


