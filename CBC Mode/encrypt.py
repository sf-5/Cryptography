from random import randint

def XOR(k, m):
    c = []
    for i in range(7):
        if k[i] == m[i]:
            c.append('0')

        else:
            c.append('1')

    return ''.join(c)

def F(k, m):
    return(XOR(k, m))

def Enc(k, m):
    c = [[]]
    for i in range(7):
        c[0].append(str(randint(0,1)))
    
    c[0] = ''.join(c[0])
    
    for i in range(len(m)):
        c.append(F(k, XOR(m[i], c[i])))

    return c

plaintext = input("Enter desired message: ")

m = []
for char in plaintext:
    bin_char = bin(ord(char))[2:]
    if len(bin_char) < 7:
        bin_char = "0" + bin_char
    m.append(bin_char)

k = []
for i in range(7):
        k.append(str(randint(0,1)))

print("Your key is:", ''.join(k))

c = Enc(k, m)

with open('encrypted.txt', 'w') as encrypted_file:
    encrypted_file.write(''.join(c))