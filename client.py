import socket
import tqdm
import os

from cryptography.fernet import Fernet
import time

import random, string
import pickle
import time

import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
 
class rsa_en_de():
    
    def createkey(self):
        publicKey, privateKey = rsa.newkeys(2048)
        return publicKey, privateKey
    
    def savekey(self, pubkey, pubkey_name, privkey, privkey_name):
        publicKeyPkcs1PEM = pubkey.save_pkcs1().decode('utf8') 
        
        privateKeyPkcs1PEM = privkey.save_pkcs1().decode('utf8')
        
        writeKey = open(pubkey_name, "w")
        writeKey.write(publicKeyPkcs1PEM)
        writeKey.close()
        
        writeKey = open(privkey_name, "w")
        writeKey.write(privateKeyPkcs1PEM)
        writeKey.close()
        
        
            
    def keyload(self, pubkey_name, privkey_name):
        readKey = open(pubkey_name, "r")
        public=readKey.read()
        readKey.close()
        
        readKey = open(privkey_name, "r")
        private=readKey.read()
        readKey.close()
        
        publicKeyReloaded = rsa.PublicKey.load_pkcs1(public.encode('utf8')) 
        privateKeyReloaded = rsa.PrivateKey.load_pkcs1(private.encode('utf8')) 
        return privateKeyReloaded, publicKeyReloaded
    
    def en(self, filename, pubkey, enc_file):
        start = time.time()
        with open(filename, 'r') as txt:
            text = txt.read()
        
        encMessage = rsa.encrypt(text.encode(), pubkey)
        
        binary_file = open(enc_file, "wb")
        binary_file.write(encMessage)
        binary_file.close()
        end = time.time()
        print(end - start)
        
        return encMessage
    
    def de(self, enc_file, privkey, dec_file):
        binary_file = open(enc_file, "rb")
        encMessage=binary_file.read()
        binary_file.close()
        
        decMessage = rsa.decrypt(encMessage, privkey).decode()
        with open(dec_file, 'w') as txt:
            txt.write(decMessage)
            
            
class EncryptorNoLib():
    def read_file(self, filename):
        with open(filename, 'r') as file:
            original = file.read()
            length = len(str(original))
            return original, length
        
    def generate_key(self, length, keyname):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        with open(keyname, 'w') as mykey:
            mykey.write(key)
    
    def key_load(self, keyname):
        with open(keyname, 'r') as mykey:
            key = mykey.read()
        return key
    
    def encryption(self, load_key, load_file, en_file):
        start = time.time()
        e_list = [chr(ord(a) ^ ord(b)) for a,b in zip(load_file, load_key)]
        
        # end = time.time()
        # print(end - start)
        
        with open(en_file, "wb") as fp:
            pickle.dump(e_list, fp)
            
        end = time.time()
        print(end - start)
            
    def decryption(self, load_key, en_file, de_file):
        
        with open(en_file, "rb") as fp:   # Unpickling
            rde_file = pickle.load(fp)
        
        de_list = [chr(ord(a) ^ ord(b)) for a,b in zip(rde_file, load_key)]
        text = "".join(de_list)
        
        # print(text)
        
        with open(de_file, 'w') as file:
            file.write(text)

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


    def file_encrypt(self, key, original_file, encrypted_file):
        start = time.time()
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)
            
        end = time.time()
        print(end - start)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)
            
encryptor=Encryptor()
encryptorNolib=EncryptorNoLib()
rsa_enc=rsa_en_de()

# mykey=encryptor.key_create()
# encryptor.key_write(mykey, 'mykey.key')
# loaded_key=encryptor.key_load('mykey.key')
# encryptor.file_encrypt(loaded_key, 'Galois.txt', 'E_Galois.txt')


# load_txt, length = encryptorNolib.read_file('Galois.txt')
# encryptorNolib.generate_key(length, 'keynolib.txt')
# key = encryptorNolib.key_load('keynolib.txt')
# encryptorNolib.encryption(str(key), str(load_txt), 'en_file')
# encryptorNolib.decryption(str(key), 'en_file', 'de_file.txt')

files = []

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "127.0.0.1"
# the port, let's use 5001
port = 8081
# the name of file we want to send, make sure it exists
raw_filename = input('Select file : ')

method = input("Encryption Method\n a. Using Library\n b. Using No Library \n c. RSA\nWhich method would you prefer : ")

output = 'Encrypted.txt'
output_nolib = 'Encrypted'

if (method == 'a'):
    #Using Library
    mykey=encryptor.key_create()
    encryptor.key_write(mykey, 'mykey.key')
    loaded_key=encryptor.key_load('mykey.key')
    encryptor.file_encrypt(loaded_key, raw_filename, output)
    filename = output

elif (method == 'b'):
    #Using No Library
    load_txt, length = encryptorNolib.read_file(raw_filename)
    encryptorNolib.generate_key(length, 'keynolib.txt')
    key = encryptorNolib.key_load('keynolib.txt')
    encryptorNolib.encryption(str(key), str(load_txt), output_nolib)
    # encryptorNolib.decryption(str(key), 'en_file', 'de_file.txt')
    
    filename = output_nolib
    
elif (method == 'c'):
    pubkey, privkey = rsa_enc.createkey()
    rsa_enc.savekey(pubkey,'public key.pem', privkey, 'private key.pem')
    privkey, pubkey = rsa_enc.keyload('public key.pem', 'private key.pem')
    print(rsa_enc.en(raw_filename, pubkey, output))
    # print(rsa_enc.de('Galois_RSA_En.txt', privkey, 'Galois_RSA_De.txt'))
    
    filename = output
    

    

#Using RSA

# files.append('E_Galois.txt')
# files.append('mykey.key')


# filename = 'E_Galois.txt'

# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()