def maze_solver(n, path):
	maze = [['.' for _ in range(n)] for _ in range(m+1)]
	row =0
	col = 0
	maze[row][col] = '*'
	for move in path:
		if move == 'R':
			if col<n-1:
				col += 1
		elif move == 'L':
			if col-1 >=0:
				col -= 1
		elif move == 'B':
			row += 1
		maze[row][col] = '*'
	for row in maze:
		print(' '.join(row))
	if col != n-1:
		print("There's no way out!")
n = int(input( ))
path=[ ]
while True :
	path1 = input( )
	if path1=='END':
		break
	elif path1 in ['R','L','B']:
		path.append(path1)
m=0
for path1 in path:
	if path1=='B':
		m +=1
result =maze_solver(n, path)
