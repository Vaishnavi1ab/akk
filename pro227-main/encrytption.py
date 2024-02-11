passcode="!@#$%^&*()_+"   

key_token=["Ra7hG6MWr", "o6pHzyss3", "jADypc7jb", "yqW7XzlbK", "zaWn6oTht", "axObrINre", 
 "vOxTF6fBi", "gPFqofs7j", "ifKHiEYeS", "qTDvTnfa2", "82846kmi9", "iHDAR1dm6", "g8jPGje0H", "6qliLl4Mo", "NQr4uSGzQ", "0YSxtLoXw", "BXLfrOS9f", "WHlAtPKed", 
 "yvP930L5E", "OuRJHlCAn", "PQe3NDDkz", "PEpQdMkr6", "7Kw4GQHsh", "e3E36kmmL", "0wMa5eTK8", "9W6IEM4qe", "WmH4h4QF3", "edOzFOsWq", "yjCzBo8r6", "Iz2CZYfl5", "ofKPdqmPZ", "ZyFSPO294", "J6zCyyiaO", 
 "xBmBOwBl3", "NfCGmrcQy", "asdasd"]

key_char = ['0', '1', '2', '3', '4', '5', '6' '7', '8', '9',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'," "]
def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        print("Wrong Choice")

def encrypt():
    print("encryption")
    m = input("enter: ")
    ml = list(m)
    en_txt =""
    for i in ml:
        g = key_char.index(i)
        for h in key_token:
            k = key_token.index(h)
            if g == k:
                en_txt+=h+" "
        
    print(en_txt)
    
def decrypt():
    print("decryption")
    m = input("enter: ")
    ml = m.split()
    de_en_txt =""
    for i in ml:
        g = key_token.index(i)
        for h in key_char:
            k = key_char.index(h)
            if g == k:
                de_en_txt+=h
    pas = input("enter the password for decryption: ")
    if pas == passcode:    
        print(de_en_txt)
    else:
        print("access denied")
    
if __name__ == "__main__":
    main()