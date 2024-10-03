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

def Dec(k, c_str):
    c = []
    for i in range(0, len(c_str), 7):
        c.append(c_str[i:i+7])
    
    m = []
    for i in range(1, len(c)):
        m.append(XOR(c[i-1], F(k, c[i])))

    return m

with open('encrypted.txt', 'r') as encrypted_file:
    c = encrypted_file.read()

k = input("Please enter your key: ")

m = Dec(k, c)

plaintext = []
for bin_char in m:
    char = chr(int(bin_char, 2))
    plaintext.append(char)

print(''.join(plaintext))