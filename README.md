# Diffie-Helman
## What is Diffie-Helman
>Diffie–Hellman key exchange is a method of securely exchanging cryptographic keys over a public channel and was one of the first public-key protocols as conceived by Ralph Merkle and named after Whitfield Diffie and Martin Hellman. DH is one of the earliest practical examples of public key exchange implemented within the field of cryptography.<br/>
-_from [wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)_

## What is done in this implementation
>In the following implementation of the program, the client and server communicate using socket programming, but before the message is sent it is encrypted using the shift cipher technique which has been implemented in the `ShiftCipher.py` file, and once the message is received on either side it is decrypted again using the function in `ShiftCipher.py`.<br/><br/>
>The file `Diffie-Helman.py` is just the plain implementation of Diffie-Helamn's Algorithm, in the program it takes the necessary inputs, computes and gives the results which is `Ka` and `Kb` to be verified by the user.

## To run the program
1. Download/clone the repo in your system.
2. Make sure the files `DH-Server.py`, `DH-Client.py` and `ShiftCipher.py` are in the same directory.
3. Open Command Prompt [Windows] and Terminal [Ubuntu] and run the `DH-Server.py` in the respective platform.
4. Now run the `DH-Client.py` once you have provided all the necessary inputs to the **Server** program and provide the required inputs for the **Client** program.
5. The program will display the `Ka` and `Kb` respectively, and then you can proceed with the further chatting.
6. If you want to close the connection or stop the communication you can press ***Ctrl+c*** or just type **'bye'** without quotes on the client side.
