n = int (input ("Enter the number of rows and columns for the square matrix: "))
print ("Start entering the elements of the matrix each one in a separate line")
def rot (matrix, degrees):
    while (degrees < 0): #if user wants to rotate anti-clockwise
        degrees += 360

    while (degrees > 360):
        degrees -= 360

    l = 0
    t = 0
    r = n - 1
    b = n - 1

    while (degrees > 0):
        while (l < r):
            for i in range (r - l):
                x = matrix [t][l + i]
                matrix [t][l + i] = matrix [b - i][l]
                matrix [b - i][l] = matrix [b][r - i]
                matrix [b][r - i] = matrix [t + i][r]
                matrix [t + i][r] = x
                
            l += 1
            t += 1
            r -= 1
            b -= 1
            
        degrees -= 90

    return matrix

matrix = []
for i in range (n):
    m = []
    for j in range (n):
        m.append (int (input ()))
    matrix.append (m)

print ("The matrix you entered: ")
for i in range (n):
    for j in range (n):
        print (matrix [i][j], end = ' ')
    print ()

degrees = int (input ("Enter the degrees you want to turn the matrix clockwise: "))
matrix = rot (matrix, degrees)

for i in range (n):
    for j in range (n):
        print (matrix [i][j], end = ' ')
    print ()
