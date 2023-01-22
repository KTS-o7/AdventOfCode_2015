def minArea(face1, face2 , face3):
    if(face1<face2):
        if(face1<face3):
            return face1
        else:
            return face3
    else:
        if(face2<face3):
            return face2
        else:
            return face3
        


def wrappingArea ( length , breadth , height):
    area = 2*(length*breadth + breadth*height + height*length)
    slack = minArea(length*breadth , breadth*height ,height*length)
    return (area + slack)

def riblen( length , breadth , height):
    len1 = min(length,breadth)
    len2 = min(breadth,height)
    if len1 == len2:
        len2 = min(length,height)
    vol = length*breadth*height
    lengthOfRib = (2*(len1+len2))+vol
    return lengthOfRib


def main():
    filehandle = open("Advent_of_code_2015/2015_prob2_input.txt")
    totarea =0
    riblength = 0
    for exp in filehandle:
        nums = list(map(int,exp.split('x')))
        totarea = totarea + wrappingArea(nums[0],nums[1],nums[2])
        riblength = riblength + riblen(nums[0],nums[1],nums[2])
    print("\n",totarea,"\n")
    print("\n",riblength,"\n") 
    
  
        
   
    

main()