


filehand = "Advent_of_code_2015/2015_prob1_input.txt"
fd = open(filehand)
inputstring = fd.read()
k = 0
for obj in inputstring:
    if obj == '(':
        k = k+1
    if obj == ')':
        k = k-1
print("\n",k,"\n")
