from PIL import Image, ImageDraw
images = []

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
        
def draw_matrix(a,m, the_path = []):
    im = Image.new('RGB', (zoom * len(a[0]), zoom * len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    for i in range(len(a)):
        for j in range(len(a[i])):
            color = (255, 255, 255)
            r = 0
            if a[i][j] == 1:
                color = (0, 0, 0)
            if i == starting_point[0] and j == starting_point[1]:
                color = (0, 255, 0)
                r = borders
            if i == end_point[0] and j == end_point[1]:
                color = (0, 255, 0)
                r = borders
            draw.rectangle((j*zoom+r, i*zoom+r, j*zoom+zoom-r-1, i*zoom+zoom-r-1), fill=color)
            if m[i][j] > 0:
                r = borders
                draw.ellipse((j * zoom + r, i * zoom + r, j * zoom + zoom - r - 1, i * zoom + zoom - r - 1),
                               fill=(255,0,0))
    for u in range(len(the_path)-1):
        y = the_path[u][0]*zoom + int(zoom/2)
        x = the_path[u][1]*zoom + int(zoom/2)
        y1 = the_path[u+1][0]*zoom + int(zoom/2)
        x1 = the_path[u+1][1]*zoom + int(zoom/2)
        draw.line((x,y,x1,y1), fill=(255, 0,0), width=5)
    draw.rectangle((0, 0, zoom * len(a[0]), zoom * len(a)), outline=(0,255,0), width=2)
    images.append(im)

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

for i in range(10):
    if i % 2 == 0:
        draw_matrix(maze, matrix, the_path)
    else:
        draw_matrix(maze, matrix)

print_m(matrix)
print(the_path)

# Save result as .gif file
images[0].save('maze.gif',
               save_all=True, append_images=images[1:],
               optimize=False, duration=1, loop=0)
