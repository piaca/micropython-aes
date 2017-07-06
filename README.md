# micropython-aes

AES algorithm with pure python implementation. Small modify based on https://github.com/ipfans/pyAES for MicroPython.

# How to use?

### In REPL

```
>>> import maes
>>> import ubinascii
>>> 
>>> def array_tostring(array_data):
...     _string = ""
...     for _array in array_data:
...         _string = _string + chr(_array)
...     return _string
...     
>>> 
>>> key = b"1234567890abcdef"
>>> iv = b"1234567890abcdef"
>>> 
>>> cryptor = maes.new(key, maes.MODE_CBC, IV=iv)
>>> ciphertext = cryptor.encrypt(b'This is a test! What could possibly go wrong?___')
>>> print(ubinascii.b2a_base64(array_tostring(ciphertext)))
b'wo3DsMKeDTd0DXcUw4wlwq0zwrMmL8O6SxdyNsOFIcKmXk/Dty0PInYswrzCssOGwpkWATlzw54Bw6XChXXDm2ca\n'
>>> 
>>> decryptor = maes.new(key, maes.MODE_CBC, IV=iv)
>>> print(array_tostring(decryptor.decrypt(ciphertext)))
This is a test! What could possibly go wrong?___
>>> 
```

### In nodemcu with micropython

1. Fetch source code `https://github.com/micropython/micropython`
2. put `maes.py` to directory `$MICROPYTHON_DIR/esp8266/modules`
3. build firmware and flash into nodemcu

### Why?

Cause MicroPython don't support AES algorithm.

