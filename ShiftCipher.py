# importing numpy library
import numpy as np


# function for shift cipher
def shift(string, key):
    # list to store ascii values of characters
    ascii_list =[]
    for i in string:  # converting the characters to 0-255
        # using ord to get ascii values
        ascii_list.append(ord(i))  # -65)  # add to the list we made
    # covert to np array and add key, the mod 256
    # using numpy because it save you from manually coding
    ascii_list = (np.array(ascii_list) + key) % 256

    char_list = []  # list for storing chars
    for i in ascii_list:
        # chr to get char from ascii value
        char_list.append(chr(i))

    # logic from converting list to string
    cipher_text = ''
    for char in char_list:
        cipher_text += char

    # print(f'[RESULT OF SHIFT]: {cipher_text}')
    return cipher_text


# Decryption function for shift cipher
def shift_decrypt(ciphered_text, key):
    ascii_list = []
    for i in ciphered_text:  # converting the characters to 0-255
        # using ord to get ascii values
        ascii_list.append(ord(i))  # add to the list we made
    # covert to np array and add 256, subtract key, then mod 256
    ascii_list = (np.array(ascii_list) + 256 - key) % 256
    # loop for converting the numeric values to their characters
    text = ''
    for char in ascii_list:
        text += chr(char)
    return text
