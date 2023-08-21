import string
import random
 
# Untuk mendapatkan panjang password
length = int(input("Masukkan panjang password: "))
 
print('''Pilih Karakter untuk set password dari pilihan ini :
         1. Angka
         2. Huruf
         3. Spesial Karakter
         4. Exit''')
 
characterList = ""
 
# Pilih nomor untuk ngeset password
while(True):
    choice = int(input("Pilih Nomor "))
    if(choice == 1):
         
        # Memasukkan huruf ke password
        characterList += string.ascii_letters
    elif(choice == 2):
         
        # Memasukkan angka ke password
        characterList += string.digits
    elif(choice == 3):
         
        # Memasukkan spesial karakter ke password
        # characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Tolong pilih nomor yang valid!")
 
password = []
 
for i in range(length):
   
    # Mengacak untuk mendapatkan password
    # character list
    randomchar = random.choice(characterList)
     
    # memasukkan random karakter ke password
    password.append(randomchar)
 
# printing password sebagai string
print("The random password is " + "".join(password))