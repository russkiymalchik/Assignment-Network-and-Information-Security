# Assignment-Network-and-Information-Security

## Participants
Khairi Wiryawan S<br />
(05111942000023)

Muhammad Rafi Hayla Arifa<br />
(05111942000014)

## Explanation

in these Python codes, we are trying to implement encryption with following methods :<br />

### Library Method
We call ```Cryptography.fernet``` to help us encrypting text file. Fernet alone is built on top of a number of standard cryptographic primitives. Specifically it uses: AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.

### Non Library Method
In this section, we use the basic concept of logic gates
![Tex2Img_1649057590](https://user-images.githubusercontent.com/73766131/161496410-15875e32-c42c-4999-8e2c-37f7664088f1.jpg)

### RSA
For the RSA method, we call ```rsa``` library in python which construct RSA functions dedicated for python3

## Analytics
All of them gives high security to the encrypted file. but we analyze that the non library method more complex from others. the key for the encryption are generated as long as the file itself. it consumes more time in terms of generating the key alone. the output of encrypted file cannot be opened either.<br /><br />
![image](https://user-images.githubusercontent.com/73766131/161497304-c5c3abb1-3114-4bf2-9da7-0934f9293334.png)
<br />function of generating key <br /> <br />
![Screenshot (514)](https://user-images.githubusercontent.com/73766131/161497812-a5027903-76df-4c32-9612-846ed9536f8a.png)
cannot open the file <br /><br />

For time consumption, Using No library is a big win here, resulting 0.0 while RSA and Library method consumes 0.0009999275207519531 and 0.14500045776367188 respectively.
