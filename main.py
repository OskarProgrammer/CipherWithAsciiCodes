import argparse
import subprocess

parser = argparse.ArgumentParser(description="Ceasar Cipher Script")

parser.add_argument("-d","--decrypt",help="Decrypt.",required=False,type=str, default= False)

parser.add_argument("-e","--encrypt",help="Encrypt",required=False,type=str,default= False)

parser.add_argument("-s","--sentence",help="Sentence",required=True,type=str)

parser.add_argument("-k","--key",help="Key",required=True,type=int)

args = parser.parse_args()


class Encrypt(object):
    def __init__(self,sentence,key) -> None:
        self._key = key
        self._sentence = sentence

        self._result = self.encrypt()
        print(f"Result of encrypting {self._sentence} with key {self._key}: {self._result}")

    def encrypt(self) -> str:

        result = ""
        for char in self._sentence:
            result += chr(ord(char) + (self._key))

        return result

class Decrypt(object):
    def __init__(self,sentence,key) -> None:
        self._key = key
        self._sentence = sentence
        
        self._result = self.decrypt()
        print(f"Result of decrypting {self._sentence} with key {self._key}: {self._result}")

    def decrypt(self) -> str:
        result = ""
        for char in self._sentence:
            result += chr(ord(char) - (self._key))

        return result

if args.encrypt != False:
    encrypt = Encrypt(args.sentence,args.key)
elif args.decrypt != False:
    decrypt = Decrypt(args.sentence,args.key)
else:
    print("Please select either encrypt or decrypt")

