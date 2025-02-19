import os
import random
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
 
def simple_design_coffee():
    print(r"""
          
      ~ ~  ~ ~  ~ ~  ~ ~  
       (  )   (   )  )  
        ) (   )  (  (  
        ( )  (    ) )  
      ╭───────────╮__
      |   COFFEE  |  |
      ╰───────────╯

    """)

def original_design_coffee():
    print(r"""
          
      ~ ~  ~ ~  ~ ~  ~ ~
       (  )   (   )  )
        ) (   )  (  (
        ( )  (    ) )
      ╭─────────────╮__
      |  ~~~~~~~~~  |  |
      |  ( COFFEE ) |   |
      |  ~~~~~~~~~  |  |
      ╰─────────────╯

    """)

def solid_cup_design_coffee():
    print(r"""
          
      ~ ~  ~ ~  ~ ~  ~ ~  
       (  )   (   )  )  
        ) (   )  (  (  
        ( )  (    ) )  
      ╭═════════════╮__
      |  ~~~~~~~~~  |  |
      |  ( COFFEE ) |  |
      |  ~~~~~~~~~  |  |
      ╰═════════════╯

    """)

coffee_designs = [simple_design_coffee, original_design_coffee, solid_cup_design_coffee]

def success_banner():
    """Print a success ASCII banner with a green color."""
    # Change color of the console output to green
    print("\033[92m")  # ANSI escape code for green

    print("Success! You have decrypted your files.")
    coffee_design = random.choice(coffee_designs)
    coffee_design()
    print("E N J O Y  Y O U R  C O F F E E !")

    # Reset the color
    print("\033[0m")

def fail_banner():
    """Print a failure ASCII banner with a red color."""
    # Change color of the console output to red
    print("\033[91m")  # ANSI escape code for red

    print("Sorry! Wrong secret phrase!")

    print(r"""
        
        ██████╗ ███████╗███╗   ██╗██╗███████╗██████╗ ██╗
        ██╔══██╗██╔════╝████╗  ██║██║██╔════╝██╔══██╗██║
        ██║  ██║█████╗  ██╔██╗ ██║██║█████╗  ██║  ██║██║
        ██║  ██║██╔══╝  ██║╚██╗██║██║██╔══╝  ██║  ██║╚═╝
        ██████╔╝███████╗██║ ╚████║██║███████╗██████╔╝██╗

        A C C E S S   R E J E C T E D !
    """)

    # Reset the color
    print("\033[0m")

def not_encrypted_banner():
    """Print a banner stating the files are not encrypted."""
    print("\033[93m")  # ANSI escape code for yellow
    print(" Your files are not encrypted!")

    print(r"""
          
        ████████╗ █████╗ ██╗  ██╗███████╗    ██╗████████╗    ███████╗ █████╗ ███████╗██╗   ██╗
        ╚══██╔══╝██╔══██╗██║ ██╔╝██╔════╝    ██║╚══██╔══╝    ██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝
           ██║   ███████║█████╔╝ █████╗      ██║   ██║       █████╗  ███████║███████╗ ╚████╔╝ 
           ██║   ██╔══██║██╔═██╗ ██╔══╝      ██║   ██║       ██╔══╝  ██╔══██║╚════██║  ╚██╔╝  
           ██║   ██║  ██║██║  ██╗███████╗    ██║   ██║       ███████╗██║  ██║███████║   ██║   
           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
          
        N O T H I N G  IS  E N C R Y P T E D !
    """)
    print("\033[0m")

def clear_console():
    """Clear the console screen on Windows or Unix-like systems."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    if not os.path.exists("thekey.key"):
        not_encrypted_banner()
        return
    
    files = get_encrypted_files()
    secretkey = load_secret_key()
    
    secret_phrase = "coffee_break"
    user_phrase = input("Enter the secret phrase to decrypt your files \n")
    
    if user_phrase == secret_phrase:
        decrypt_files(files, secretkey)

        # Remove the key file once decryption is done
        if os.path.exists("thekey.key"):
            os.remove("thekey.key")

        clear_console()
        success_banner()
    else:
        clear_console()
        fail_banner()

if __name__ == "__main__":
    main()
