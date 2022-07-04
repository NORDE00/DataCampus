# Minimum Edit Distance
# each operation has cost of '1'

def inserter (list, n):
    count = 0
    for i in n:
        list[count][0] = i
        count += 1
    return list
    
def matrix_maker (word_1, word_2):
    global col
    global index
    
    col = [' ','#']+(list(word_1)) 
    index = [' ','#']+(list(word_2))
    
    matrix = [[0] * (len(col)) for _ in range(len(index))]
    matrix[0] = col
    matrix = inserter(matrix, index)
    
    return matrix

def starter (mat):
    counter = 0
    for i in range(len(col)):
        mat[1][i+1] = counter
        counter += 1
        if counter == len(col)-1:
            break
    counter = 0
    for j in range(len(index)):
        mat[j+1][1] = counter
        counter += 1
        if counter == len(index)-1:
            break

def add (a, b, c, par):
    return min(a,b,c) + par

def fill_m (mat, x,y): #min
    if mat[0][x] != mat[y][0]:
        mat[y][x] = add(mat[y-1][x-1],mat[y-1][x],mat[y][x-1],1)
    else:
        mat[y][x] = mat[y-1][x-1]

def MED_cal(word_1, word_2):
    matrix = matrix_maker(word_1, word_2)
    starter(matrix)
    
    for y in range(2, len(index)):
        for x in range(2,len(col)):
            fill_m(matrix,x,y)
    return matrix

def fancy_printer(list):
    for a in list:
        line = []
        for b in a:
            line.append(str(b))
        print(" ".join(line))

result = MED_cal('cake','cat')
fancy_printer(result)

'''
a, b = input().split()
list(a)
list(b)
abc = [[0] * (len(b)+1) for _ in range(len(a) + 1)]

for i in range(len(a)+1):
    abc[i][0] = i
for j in range(len(b)+1):
    abc[0][j] = j
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if(a[i-1] == b[j-1]):
            abc[i][j] = abc[i-1][j-1]
        else:
            abc[i][j] = min(abc[i-1][j-1]+2, abc[i-1][j]+1, abc[i][j-1]+1)
    for j in range(len(b)+1):
        print(abc[i][j], end = "")
    print("\n")
print(abc[len(a)][len(b)])
'''