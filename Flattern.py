input = [1,2, [3,[4,5],6],7]
output = [1,2,3,4,5,6,7]

def flattern(input):
    
    res = []
    
    for i in input:
        if isinstance(i, list):
            res.extend(flattern(i))
        else:
            res.append(i)
    
    return res
    

print(flattern(input))
