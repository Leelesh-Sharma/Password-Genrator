import random
import string

alphabets = list(string.ascii_letters)
numbers = [0,1,2,3,4,5,6,7,8,9]
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


def efficient_password():
    print('EFFICIENT PASSSWORD')
    digits = int(input('How many digits should your password may contain - '))
    
    for _ in range(digits):
        ps = random.choice(alphabets + numbers + special_ch)
        password.append(ps)
    
    count_u = count_n = count_l = count_p = 0

    for i in string.ascii_uppercase:
        for j in password:
            if i == j:
                count_u = count_u +1

    for i in string.ascii_uppercase:
        for j in password:
            if i == j:
                count_l= count_l +1
    
    for i in numbers:
        for j in password:
            if i == j:
                count_n = count_n +1

    for i in string.punctuation:
        for j in password:
            if i == j:
                count_p = count_p +1
    print(count_p)
    print(count_l)
    print(count_n)
    print(count_u)
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
    pass