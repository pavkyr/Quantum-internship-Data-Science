def dfs(grid,row,col):
  grid[row][col]=0
  lst=[(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
  for r,c in lst:
    if r>=0 and c>=0 and r<len(grid) and c<len(grid[r]) and grid[r][c]==1:
      dfs(grid,r,c)

def numIsland(grid):
  island=0
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c]==1:
        dfs(grid,r,c)
        island+=1
  return island

grid1 = [
  [1,1,1,1,0],
  [1,1,0,1,0],
  [1,1,0,0,0],
  [0,0,0,0,0]
]

grid2 = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]

print('test grid1:')
for i in grid1:
  print(i)
print(f'number of island is: {numIsland(grid1)}')

print('\n')

print('test grid2:')
for i in grid2:
  print(i)
print(f'number of island is: {numIsland(grid2)}')