
def sumDiagonalsOfSpiral(n):
    sum = 1
    val = 1
    for rectangle_size in range(3, n+1, 2):
        for j in range(4):
            val += rectangle_size -1
            sum += val
    return sum

print sumDiagonalsOfSpiral(1001)    

        

    
