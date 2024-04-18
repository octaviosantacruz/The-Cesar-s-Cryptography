from cesar import encrypt_cesar, decrypt_cesar
from cipheraffine import encrypt_affine, decrypt_affine
from vigenere import encrypt_vigenere, decrypt_vigenere
from playfair import encrypt_playfair, decrypt_playfair
from hill import encrypt_hill, decrypt_hill
CIPHER_FUNCTIONS = {
  "Cesar": {
    "encrypt": encrypt_cesar,
    "decrypt": decrypt_cesar,
    "args":{
      "key": (True, int) # True -> required, int -> data type
    }
    },
  "Affine": {
    "encrypt": encrypt_affine,
    "decrypt": decrypt_affine,
    "args": {
      "key1" : (True, int),
      "key2" : (True, int)
    }
    },
    "Vigenere": {
    "encrypt": encrypt_vigenere,
    "decrypt": decrypt_vigenere,
    "args": {
      "key": (True, str)
    },
    },
    "Playfair": {
    "encrypt": encrypt_playfair,
    "decrypt": decrypt_playfair,
    "args": {
      "keyword": (True, str) # Case-Insensitive
    }
    },
    "Hill": {
    "encrypt": encrypt_hill,
    "decrypt": decrypt_hill,
    "args": {
      "matrix": (True, list) # 3x3 matrix
    }
    },     
}
def display_menu():
    print("=============================================")
    print("   WELCOME TO MY CIPHERS SYSTEM   ")
    print("=============================================")
    for i, name in enumerate(CIPHER_FUNCTIONS.keys()):
        print(f"{i+1}. {name}")  # Print each option vertically
    print("6. Quit")
  
  
def handle_cipher_selection():
    while True:
        try:
            option = int(input("Enter your option: "))
            if 1 <= option <= len(CIPHER_FUNCTIONS) + 1:  # Correct range check
                break
            raise ValueError
        except ValueError:
            print("Invalid option. Please choose a number between 1 and", len(CIPHER_FUNCTIONS) + 1, ".")

    if option == len(CIPHER_FUNCTIONS) + 1:
        exit("Thank you for using my Cipher System. Goodbye!")
        
    # Get cipher name and arguments (only for valid cipher options)
    cipher_name = list(CIPHER_FUNCTIONS.keys())[option - 1]
    cipher_functions = CIPHER_FUNCTIONS[cipher_name]
    cipher_args = cipher_functions["args"] 
    
    # Display input prompts based on cipher arguments
    print(f"You have chosen {cipher_name} Cipher.")
    message = input("Enter the message: ")
    user_args = {}
    for arg_name, (required, data_type) in cipher_args.items():
      while True:
        try:
          arg_value = input(f"Enter {arg_name}: ")
          if required and not arg_value:
            raise ValueError
          if data_type == int:
            arg_value = int(arg_value)
          elif data_type == str:
            arg_value = arg_value.lower()
          user_args[arg_name] = arg_value
          break
        except ValueError:
          print(f"Invalid input for {arg_name}. Please try again.")
    
      # Call appropriate function with message and user-provided arguments
    if option == 1:
      encrypted_message=cipher_functions["encrypt"](message, **user_args)
      print(f"Encrypted message is : {encrypted_message}")
    elif option == 2:
      decrypted_message=cipher_functions["decrypt"](message, **user_args)
      print(f"Decrypted message is : {decrypted_message}")
    else:
      print("Invalid option.")

def main():
  while True:
    display_menu()
    handle_cipher_selection()
    
    
if __name__ == "__main__":  
  main()
  