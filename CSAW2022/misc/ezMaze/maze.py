import torch
import numpy as np
import networkx as nx
import hashlib

class Maze():
	pass

model = torch.load('maze.pt')
maze = model._modules['maze']._parameters['weight'].detach().numpy()
G = nx.Graph()
for i in range(42):
    for j in range(42):
        G.add_node((i,j))
        if i >0:
            G.add_edge((i-1,j),(i,j))
        if j>0:
            G.add_edge((i,j),(i,j-1))

for i in range(42):
    for j in range(42):
        if maze[i][j] == 1:
            G.remove_node((i,j))

path = nx.algorithms.astar_path(G,(1,0),(40,41))
wasd = ''
for i, point in enumerate(path[1:]):
	last_point = path[i]
	if point[0] == last_point[0]:
		if point[1] > last_point[1]:
			wasd += 'D'
		else:
			wasd += 'A'
	else:
		if point[0] > last_point[0]:
			wasd += 'S'
		else:
			wasd += 'W'

flag = hashlib.md5(wasd.encode('utf-8')).hexdigest()
print(wasd)
print(flag)