import json


filepath = "Advent_of_code_2015/2015_prob12_input.txt"
fd = open(filepath)
readfile =fd.read()
inputdict = json.loads(readfile)
print(len(inputdict))
