from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english

def brute_force_aes(ciphertext):
    part1 = '036'
    part2 = list(itertools.combinations_with_replacement("0123456789",6))
    part3 = '0000000'
    for sandwitch in part2:
        key = part1 + ''.join(sandwitch) + part3
        plaintext = aes_decrypt(ciphertext, key)
        if (is_english(plaintext)):
            return plaintext, key.encode()


def brutekey():
    part1 = '036'
    part2 = list(itertools.combinations_with_replacement("0123456789",6))
    part3 = '0000000'
    print(part1 + ''.join(part2[50]) + part3)


brutekey()
        
