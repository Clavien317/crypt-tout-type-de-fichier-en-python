from hashlib import sha256


entre = input("Entrer un nom de fichier\n")


sorti = input("Entrer un nom de fichier de sortie\n")

key =input("Entrer la cle :\n")

keys = sha256(key.encode('utf-8')).digest()

with open(entre, 'rb') as f_entre:
    with open (sorti,'wb') as f_sorti:
        i=0
        while f_entre.peek():
            c=ord(f_entre.read(1))
            j=i%len(keys)
            b=bytes([c^keys[j]])
            f_sorti.write(b)
            i=i+1