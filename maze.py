maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0 ,0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0 ,0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
zoom = 20
borders = 6
starting_point = 1,1
end_point = 5,19

# Function to perform a step and gives value to each step (BFS Method)
def make_step_BFS(k):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == k:
        if i>0 and matrix[i-1][j] == 0 and maze[i-1][j] == 0:
          matrix[i-1][j] = k + 1
        if j>0 and matrix[i][j-1] == 0 and maze[i][j-1] == 0:
          matrix[i][j-1] = k + 1
        if i<len(matrix)-1 and matrix[i+1][j] == 0 and maze[i+1][j] == 0:
          matrix[i+1][j] = k + 1
        if j<len(matrix[i])-1 and matrix[i][j+1] == 0 and maze[i][j+1] == 0:
           matrix[i][j+1] = k + 1

def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print( str(m[i][j]).ljust(2),end=' ')
        print()

#Create Matrix and Set starting point
matrix = []
for i in range(len(maze)):
    matrix.append([])
    for j in range(len(maze[i])):
        matrix[-1].append(0)
i,j = starting_point
matrix[i][j] = 1


# Call make_step function until it reaches end point
numOfStep = 0
while matrix[end_point[0]][end_point[1]] == 0:
    numOfStep += 1
    make_step_BFS(numOfStep)
    draw_matrix(maze, matrix)

# Take value of the end point
i, j = end_point
numOfStep = matrix[i][j]

# Print path from end to start
# by Find a neighbor cell with a value k-1 , go there, decrease k by one
the_path = [(i,j)]
while numOfStep > 1:
  if i > 0 and matrix[i - 1][j] == numOfStep-1:
    i, j = i-1, j
    the_path.append((i, j))
    numOfStep-=1
  elif j > 0 and matrix[i][j - 1] == numOfStep-1:
    i, j = i, j-1
    the_path.append((i, j))
    numOfStep-=1
  elif i < len(matrix) - 1 and matrix[i + 1][j] == numOfStep-1:
    i, j = i+1, j
    the_path.append((i, j))
    numOfStep-=1
  elif j < len(matrix[i]) - 1 and matrix[i][j + 1] == numOfStep-1:
    i, j = i, j+1
    the_path.append((i, j))
    numOfStep -= 1
  draw_matrix(maze, matrix, the_path)
