
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encryption has started")
    msg = input("Enter the message :")
    key = int(input("enter key(1-94):"))
    encrypted_text = ""
    for i in range(len(msg)):
        temp =  (ord(msg[i])+key)
        if temp>126:
            temp = temp-127+32
        encrypted_text+=chr(temp)
    print("encrypted text : "+encrypted_text)
    main()

def decryption():
    print("decryption has started ")
    print("message can only be in lowercase and uppercase alphabet!")
    e_msg = input("Enter encrypted text : ")
    d_key = int(input("enter key (1-94) : "))
    decrypted_text = ""
    for i in range(len(e_msg)):
        temp = (ord(e_msg[i])-d_key)
        if temp<32:
            temp = temp+127-32
        decrypted_text+=chr(temp)
    print("decrypted text :"+decrypted_text)
    main()




    
    

        
if __name__ == "__main__":
    main()
