plaintext = input('Слово? ')


def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for i in range(len(plaintext)):
        num = ord(plaintext[i])
        if num <= 122 and num >= 120 or num <= 90 and num >= 88:
            num -= 23
        else:
            num += 3
        ciphertext += chr(num)
    return ciphertext
print(encrypt_caesar(plaintext))
ciphertext = input('Слово?')


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for i in range(len(ciphertext)):
        num = ord(ciphertext[i])
        if num <= 99 and num >= 97 or num <= 67 and num >= 65:
            num += 23
        else:
            num -= 3
        plaintext += chr(num)
    return plaintext
print(decrypt_caesar(ciphertext))
