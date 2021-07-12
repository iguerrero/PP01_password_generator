# Simple Password Generator
import string
import random

passwd = ''

def generate_password(length=8, addsyms=True, addnums=True):
    passwd = ''
    nums = ''
    syms = ''
    if addsyms:
        syms = string.punctuation
    if addnums:
        nums = string.digits
    for i in range(length):
        passwd += random.choice(string.ascii_letters + nums + syms)
    return passwd
