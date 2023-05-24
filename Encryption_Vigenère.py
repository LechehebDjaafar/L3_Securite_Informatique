# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -Age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------


#Parameters
list_alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def reuter_number_position_Alphabet(car,list_alphabet=list_alphabet):
    if type(car) == str :
        return list_alphabet.index(car.lower())
    else :
        if car > 25 :
            return list_alphabet[(car-25)-1]
        return list_alphabet[car]

        

#Create a text encryption function with encryption vigenère
def encrypt_vigenere(text,key,list_alphabet=list_alphabet,encrypt_text="",i=0):
    for car in text:
        position_car_in_text=reuter_number_position_Alphabet(car)
        position_car_in_Key=reuter_number_position_Alphabet(key[i])
        number_sign = position_car_in_text+position_car_in_Key
        encrypt_text+=reuter_number_position_Alphabet(number_sign)
        if (len(key)-1) == i:
            i=0
        else:
            i+=1
    return encrypt_text


#Create a text decryption function with decryption vigenère
def decrypt_vigenere(text,key,list_alphabet=list_alphabet,decrypt_text="",i=0):
    for car in text:
        position_car_in_text=reuter_number_position_Alphabet(car)
        position_car_in_Key=reuter_number_position_Alphabet(key[i])
        number_sign = position_car_in_text-position_car_in_Key
        decrypt_text+=reuter_number_position_Alphabet(number_sign)
        if (len(key)-1) == i:
            i=0
        else:
            i+=1
    return decrypt_text


#Create a function with get key in decryption vigenère
def get_encryption_key(encrypt_text,decrypt_text,key=""):
    for num_car in range(len(encrypt_text)):
        position_car_in_encrypt_text=reuter_number_position_Alphabet(encrypt_text[num_car])
        position_car_in_decrypt_text=reuter_number_position_Alphabet( decrypt_text[num_car])
        number_sign = position_car_in_decrypt_text-position_car_in_encrypt_text
        key+=reuter_number_position_Alphabet(number_sign)
    return key

def main():
    print("Welcome to Text Encryption System!")
    print("=================================")
    print("Options:")
    print("1. Encrypt the text")
    print("2. Decrypt the text")
    print("3. Find the encryption key")
    print("=================================")

    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))

            if choice == 1:
                encrypt_text()
                valid_choice = True
            elif choice == 2:
                decrypt_text()
                valid_choice = True
            elif choice == 3:
                find_encryption_key()
                valid_choice = True
            else:
                print("\033[1;31mInvalid choice. Please try again.")
        except:
            print("\033[1;31mInvalid choice. Please try again.")



def encrypt_text():
    text = input("Enter the text you want to encrypt: ")
    key = input("Enter the encryption key: ")
    print("Encrypting the text...")
    print(f"your text encrypted is: {encrypt_vigenere(text, key)}")


def decrypt_text():
    text = input("Enter the text you want to decrypt: ")
    key = input("Enter the encryption key: ")
    print("Decrypting the text...")
    print(f"your text decrypted is: {decrypt_vigenere(text, key)}")

def find_encryption_key():
    unencrypted_text = input("Enter the unencrypted text: ")
    encrypted_text = input("Enter the encrypted text: ")
    print("Finding the encryption key...")
    print(f" encryption key is : {get_encryption_key(unencrypted_text, encrypted_text)} ")
    
# Call the main function
main()