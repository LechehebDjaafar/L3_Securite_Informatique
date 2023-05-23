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
        number_sign = position_car_in_text-position_car_in_Key
        encrypt_text+=reuter_number_position_Alphabet(number_sign)
        if (len(key)-1) == i:
            i=0
        else:
            i+=1
    return encrypt_text


#Create a text decryption function with decryption vigenère
def decrypt_vigenere(text,key,list_alphabet=list_alphabet,encrypt_text="",i=0):
    for car in text:
        position_car_in_text=reuter_number_position_Alphabet(car)
        position_car_in_Key=reuter_number_position_Alphabet(key[i])
        number_sign = position_car_in_text-position_car_in_Key
        encrypt_text+=reuter_number_position_Alphabet(number_sign)
        if (len(key)-1) == i:
            i=0
        else:
            i+=1
    return encrypt_text


#Create a function with get key in decryption vigenère
def get_Key(encrypt_text="specialiteinformatique",decrypt_text="dxggvcptbgmahscucxvsyp",key=""):
    for num_car in range(len(encrypt_text)):
        position_car_in_encrypt_text=reuter_number_position_Alphabet(encrypt_text[num_car])
        position_car_in_decrypt_text=reuter_number_position_Alphabet( decrypt_text[num_car])
        number_sign = position_car_in_decrypt_text-position_car_in_encrypt_text
        key+=reuter_number_position_Alphabet(number_sign)
    return key


