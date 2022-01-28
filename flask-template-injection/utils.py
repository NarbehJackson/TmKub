from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os


class Crypt:
    def __init__(self):
        self.salt = os.environ.get('SALT')
        self.key = os.environ.get('ENC_KEY') 
        self.enc_dec_method = 'utf-8'       

    def encrypt(self, data):
        obj = AES.new(self.key, AES.MODE_CFB, self.salt)
        enc = obj.encrypt(data)
        value = b64encode(enc).decode(self.enc_dec_method)
        return value        

    def decrypt(self, enc_str):
        obj = AES.new(self.key, AES.MODE_CFB, self.salt)
        str_tmp = b64decode(enc_str.encode(self.enc_dec_method))
        str_dec = obj.decrypt(str_tmp)
        value = str_dec.decode(self.enc_dec_method)
        return value