from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os
import sys

card_number = sys.argv[1]

salt = os.environ.get('SALT')
key = os.environ.get('ENC_KEY') 
encoding = 'utf-8'

obj = AES.new(key, AES.MODE_CFB, salt)
str_tmp = b64decode(card_number.encode(encoding))
str_dec = obj.decrypt(str_tmp)
value = str_dec.decode(encoding)
print(value)
