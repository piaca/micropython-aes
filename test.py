# encoding: utf-8

import maes
import ubinascii

def array_tostring(array_data):
    _string = ""
    for _array in array_data:
        _string = _string + chr(_array)
    return _string

key = b"1234567890abcdef"
iv = b"1234567890abcdef"

cryptor = maes.new(key, maes.MODE_CBC, IV=iv)
ciphertext = cryptor.encrypt(b'This is a test! What could possibly go wrong?___')
print(ubinascii.b2a_base64(array_tostring(ciphertext)))

decryptor = maes.new(key, maes.MODE_CBC, IV=iv)
print(array_tostring(decryptor.decrypt(ciphertext)))