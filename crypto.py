
import string
import random

# Create a mapping for encryption
plain_chars = string.ascii_letters + string.digits + "@#$"
enc_list = list(plain_chars)
random.shuffle(enc_list)
enc_chars = ''.join(enc_list)

encrypt_map = dict(zip(plain_chars, enc_chars))
decrypt_map = dict(zip(enc_chars, plain_chars))

def encrypt_text(text):
    result = ""
    for ch in text:
        result += encrypt_map.get(ch, ch)
    return result

def decrypt_text(text):
    result = ""
    for ch in text:
        result += decrypt_map.get(ch, ch)
    return result


def hash_text(text):
    total = 0
    for ch in text:
        total += ord(ch)
    return "HASH" + str(total)
