# Simple Password Generator
import string
import random

passwd = ''

def generate_password(length=8, addsyms=True, addnums=True):
    '''
    Generates by default an 8 characters long password. You can change the length of the password
    and choose whether you want numbers or symbols.
    '''

    passwd = ''
    nums = ''
    syms = ''
    if addsyms:
        syms = string.punctuation
    if addnums:
        nums = string.digits
    for _ in range(length):
        passwd += random.choice(string.ascii_letters + nums + syms)
    return passwd

if __name__=='__main__':
    generate_password()
