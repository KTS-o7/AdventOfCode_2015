def onlySanta():
    filehandle = "Advent_of_code_2015/2015_prob3_input.txt"
    fd =open(filehandle)
    inputString  = fd.read()

    cordinates=[0,0]
    visited = [[0,0]]
    
    for ind in range(0,len(inputString)):
        if inputString[ind] == "^":
            cordinates[1] = cordinates[1]+1
        if inputString[ind] == "v":
            cordinates[1] = cordinates[1]-1
        if inputString[ind] == ">":
            cordinates[0] = cordinates[0]+1
        if inputString[ind] == "<":
            cordinates[0] = cordinates[0]-1 
        if cordinates not in visited:
            visited.append([cordinates[0],cordinates[1]])
    

    print(len(visited))

def santaAndRoboSanta():
    filehandle = "Advent_of_code/2015_prob3_input.txt"
    fd =open(filehandle)
    inputString  = fd.read()
    
    santa = True
    santaCords = [0,0]
    roboCords  = [0,0]
    visited = [[0,0]]
    
    for ind in range(0,len(inputString)):
        if santa:
            if inputString[ind] == "^":
                santaCords[1] = santaCords[1]+1
            if inputString[ind] == "v":
                santaCords[1] = santaCords[1]-1
            if inputString[ind] == ">":
                santaCords[0] = santaCords[0]+1
            if inputString[ind] == "<":
                santaCords[0] = santaCords[0]-1 
            if santaCords not in visited:
                visited.append([santaCords[0],santaCords[1]])
            santa = False
        else:
            if inputString[ind] == "^":
                roboCords[1] = roboCords[1]+1
            if inputString[ind] == "v":
                roboCords[1] = roboCords[1]-1
            if inputString[ind] == ">":
                roboCords[0] = roboCords[0]+1
            if inputString[ind] == "<":
                roboCords[0] = roboCords[0]-1 
            if roboCords not in visited:
                visited.append([roboCords[0],roboCords[1]])
            santa = True
    
    print(visited)
    print(len(visited))


santaAndRoboSanta()