def vowels(inputString):
    count =0
    for ind in range(0,len(inputString)):
        if inputString[ind] == "a" or inputString[ind] == "e" or inputString[ind] == "i" or inputString[ind] == "o" or inputString[ind] == "u":
            count = count +1
    if count<3:
            return 0
    else:
            return 1
    
   
def forbiddenDuo(inputString):
    if "ab" in inputString or "cd" in inputString or "pq" in inputString or "xy" in inputString :
        return 0
    else:
        return 1
    
def doubleChar(inputString):
    if "aa" in inputString or "bb" in inputString or "cc" in inputString or "dd" in inputString or "ee" in inputString or "ff" in inputString or "gg" in inputString or "hh" in inputString or "ii" in inputString or "jj" in inputString or "kk" in inputString or "ll" in inputString or "mm" in inputString or "nn" in inputString or "oo" in inputString or "pp" in inputString or "qq" in inputString or "rr" in inputString or "ss" in inputString or "tt" in inputString or "uu" in inputString or "vv" in inputString or "ww" in inputString or "xx" in inputString or "yy" in inputString  or "zz" in inputString :
        return 1
    else:
        return 0
    
def main():
    filepath = "Advent_of_code_2015/2015_prob5_input.txt"
    fd =open(filepath)
    readfile = fd.read()
    inputlist = list(map(str,readfile.split()))
    nice =0
    naughty =0
    
    for obj in inputlist:
        if(int(vowels(obj)) and int(doubleChar(obj)) and int(forbiddenDuo(obj))):
            nice = nice+1
        else:
            naughty = naughty+1        
    print("Nice count is ",nice)
    print("Naughty count is ",naughty)


main()