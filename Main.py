import random
import string

alphabets = list(string.ascii_letters)
numbers = list(string.digits)
special_ch = list(string.punctuation)

password = list()
    
def normal_password():    
    print('NORMAL PASSWORD')
    digits = int(input('How many digits should your password may contain - '))
    
    for _ in range(digits):
        ps = random.choice(alphabets + numbers + special_ch)
        password.append(ps)
    
    for p in password:
        print(p,end="")


def super_strong_password():
    print('SUPER STRONG PASSWORD')
    digits = int(input('How many digits should your password may contain - '))
    
    for _ in range(digits):
        ps = random.choice(special_ch)
        password.append(ps)
    
    for p in password:
        print(p,end="")


if __name__ == '__main__':
    normal_password()