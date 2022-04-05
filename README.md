# Assignment-Network-and-Information-Security

## Participants
Khairi Wiryawan S<br />
(05111942000023)

Muhammad Rafi Hayla Arifa<br />
(05111942000014)

## Explanation

in these Python codes, we are trying to implement encryption with following methods :<br />

### Library Method
We call ```Cryptography.fernet``` to help us encrypting text file. Fernet alone is built on top of a number of standard cryptographic primitives. Specifically it uses: AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.<br />
![image](https://user-images.githubusercontent.com/73766131/161852415-6767748c-6645-4dfc-a040-6e712c308ac2.png)<br />


### Non Library Method
In this section, we use the basic concept of logic gates
![Tex2Img_1649057590](https://user-images.githubusercontent.com/73766131/161496410-15875e32-c42c-4999-8e2c-37f7664088f1.jpg)<br />
![image](https://user-images.githubusercontent.com/73766131/161852610-521dfc4d-29c0-4c0d-ab47-66447a7e877d.png)<br />


### RSA
For the RSA method, we call ```rsa``` library in python which construct RSA functions dedicated for python3

## Analytics
All of them gives high security to the encrypted file. but we analyze that the non library method more complex from others. the key for the encryption are generated as long as the file itself. it consumes more time in terms of generating the key alone. the output of encrypted file cannot be opened either.<br /><br />
![image](https://user-images.githubusercontent.com/73766131/161497304-c5c3abb1-3114-4bf2-9da7-0934f9293334.png)
<br />function of generating key <br /> <br />
![Screenshot (514)](https://user-images.githubusercontent.com/73766131/161497812-a5027903-76df-4c32-9612-846ed9536f8a.png)
cannot open the file <br /><br />

but, RSA quite difficult as well in terms of Encryption. you can see the result as follows<br />
![image](https://user-images.githubusercontent.com/73766131/161500246-1c5e5f02-4317-44ef-b9e7-d7030ce4494b.png)

while Library method you can see as follows <br />
![image](https://user-images.githubusercontent.com/73766131/161500453-b61f7b14-544e-498d-bf66-f6b553c3c0f3.png)


For time consumption, Using No library is a big win here, resulting 0.0 while RSA and Library method consumes 0.0009999275207519531 and 0.14500045776367188 respectively.<br />
![1649055897216](https://user-images.githubusercontent.com/73766131/161499720-3c7d77e0-4a1c-44f5-8eda-522bc09447cc.jpg)
![1649055939733](https://user-images.githubusercontent.com/73766131/161499751-2168cbd4-e95a-4bde-91fe-d8d0b5a1bf32.jpg)
![1649056088192](https://user-images.githubusercontent.com/73766131/161499766-8480960e-c5e4-4517-8b64-c12337f79eeb.jpg)
