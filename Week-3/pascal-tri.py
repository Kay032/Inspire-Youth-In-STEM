
num_rows = 10


triangle = [[1]]


for i in range(1, num_rows):
    row = [1] 
    for j in range(1, i):
        
        element = triangle[i-1][j-1] + triangle[i-1][j]
        row.append(element)
    row.append(1) 
    triangle.append(row)

for row in triangle:
    print(row)
