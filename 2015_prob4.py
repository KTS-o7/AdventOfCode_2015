import hashlib as hl
string ="yzbqklnj"

def fiveZeroes():
    val = True
    i = 0
    while(val):
        string1 = string+str(i)
        #print(string1)
        i =  i+1
        hashedVal = hl.md5(string1.encode())
        hexval = hashedVal.hexdigest()
        check = hexval[0:5]
        if check == "00000":
            val = False
    print(check)
    print(string1)


def sixZeroes():
    val = True
    i = 0
    while(val):
        string1 = string+str(i)
        #print(string1)
        i =  i+1
        hashedVal = hl.md5(string1.encode())
        hexval = hashedVal.hexdigest()
        check = hexval[0:6]
        if check == "000000":
            val = False
    print(check)
    print(string1)


fiveZeroes()