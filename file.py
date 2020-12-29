alphabet = "abcdefghijklmnopqrstuvwxyz"
symbol = "~`!@#$%^&*()_-+=;:'\",.? "


def vigenere(message, keyword):
    """This is a function for decrypting a message

    Args:
        message (string): message that going to be decrypted
        keyword (string): a keyword for decrypting the message

    Returns:
        string: decrypted message
    """

    pointer = 0
    keyworded = ""
    decoded = ""
    for i in range(len(message)):
        if not message[i] in symbol:
            keyworded += keyword[pointer]
            pointer = (pointer + 1) % len(keyword)
        else:
            keyworded += message[i]
    for i in range(len(message)):
        if not message[i] in symbol:
            lenght = alphabet.find(message[i]) - alphabet.find(keyworded[i])
            decoded += alphabet[lenght % 26]
        else:
            decoded += message[i]
    return decoded


def vigenere_coder(message, keyword):
    """This is a function for encrypting a message

    Args:
        message (string): message that going to be encrypted
        keyword (string): a keyword for encrypting the message

    Returns:
        string: encrypted message
    """

    pointer = 0
    keyworded = ""
    coded = ""
    for i in range(len(message)):
        if not message[i] in symbol:
            keyworded += keyword[pointer]
            pointer = (pointer + 1) % len(keyword)
        else:
            keyworded += message[i]
    for i in range(len(message)):
        if not message[i] in symbol:
            length = alphabet.find(message[i]) + alphabet.find(keyworded[i])
            coded += alphabet[length % 26]
        else:
            coded += message[i]
    return coded


def text_cleaner(list):
    clean_list = []
    for line in list:
        clean_list.append(line.strip("\n"))
    return clean_list


with open('text.txt') as text:
    list_text = text.readlines()

enc = text_cleaner(list_text)
with open('encrypted.txt', "w") as encrypted:
    for line in enc:
        encrypted.write(vigenere(line, "penzragon"))
        encrypted.write("\n")

with open("encrypted.txt") as text:
    enc_list = text.readlines()

dec = text_cleaner(enc_list)
with open("decrypted.txt", "w") as decrypted:
    for line in dec:
        decrypted.write(vigenere_coder(line, "penzragon"))
        decrypted.write("\n")
