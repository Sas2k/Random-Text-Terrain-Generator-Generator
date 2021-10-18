from random import*

A = []
B = []
C = []

def line_one():
    a = randint(1, 5)
    if a == 1:
        A.append('G')#ground
    if a == 2:
        A.append('R')#Rocks
    if a == 3:
        A.append('W')#Water
    if a == 4:
        A.append('S')#Sand
    if a == 5:
        A.append('M')#Mountain
    b = randint(1, 5)
    if b == 1:
        A.append('G')#ground
    if b == 2:
        A.append('R')#Rocks
    if b == 3:
        A.append('W')#Water
    if b == 4:
        A.append('S')#Sand
    if b == 5:
        A.append('M')#Mountain
    c = randint(1, 5)
    if c == 1:
        A.append('G')#ground
    if c == 2:
        A.append('R')#Rocks
    if c == 3:
        A.append('W')#Water
    if c == 4:
        A.append('S')#Sand
    if c == 5:
        A.append('M')#Mountain
    print(A)

def line_two():
    d = randint(1, 5)
    if d == 1:
        B.append('G')#ground
    if d == 2:
        B.append('R')#Rocks
    if d == 3:
        B.append('W')#Water
    if d == 4:
        B.append('S')#Sand
    if d == 5:
        B.append('M')#Mountain
    e = randint(1, 5)
    if e == 1:
        B.append('G')#ground
    if e == 2:
        B.append('R')#Rocks
    if e == 3:
        B.append('W')#Water
    if e == 4:
        B.append('S')#Sand
    if e == 5:
        B.append('M')#Mountain
    f = randint(1, 5)
    if f == 1:
        B.append('G')#ground
    if f == 2:
        B.append('R')#Rocks
    if f == 3:
        B.append('W')#Water
    if f == 4:
        B.append('S')#Sand
    if f == 5:
        B.append('M')#Mountain
    print(B)
def line_three():
    g = randint(1, 5)
    if g == 1:
        C.append('G')#ground
    if g == 2:
        C.append('R')#Rocks
    if g == 3:
        C.append('W')#Water
    if g == 4:
        C.append('S')#Sand
    if g == 5:
        C.append('M')#Mountain
    h = randint(1, 5)
    if h == 1:
        C.append('G')#ground
    if h == 2:
        C.append('R')#Rocks
    if h == 3:
        C.append('W')#Water
    if h == 4:
        C.append('S')#Sand
    if h == 5:
        C.append('M')#Mountain
    i = randint(1, 5)
    if i == 1:
        C.append('G')#ground
    if i == 2:
        C.append('R')#Rocks
    if i == 3:
        C.append('W')#Water
    if i == 4:
        C.append('S')#Sand
    if i == 5:
        C.append('M')#Mountain
    print(C)

ask = input('do you want to generate terrain[y/n]')
if ask == 'y':
    line_one()
    line_two()
    line_three()
    A = []
    B = []
    C = []
    ak = input('do you want to generate terrain[y/n]')
    if ak == 'y':
        line_one()
        line_two()
        line_three()
        A = []
        B = []
        C = []
        Ask = input('do you want to generate terrain[y/n]')
        if Ask == 'y':
            line_one()
            line_two()
            line_three()
        elif Ask == 'n':
            print('have a nice day')
    elif ak == 'n':
        print('have a nice day')

elif ask == 'n':
    print('have a nice day')
print('good day')