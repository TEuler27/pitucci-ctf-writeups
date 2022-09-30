# ezMaze

### Author

Member of r3kapig

### Description

Pytorch is a widely used AI framework. I use it as a carrier to provide a simple and interesting game. I hope you like it. The flag is md5(the shortest path of the maze).
 
## Solution
 
First of all we loaded the Pytorch model in python as follows:
```
import torch
model = torch.load('maze.pt')
```
This code gave us a strange error that we bypassed by adding 
```
class Maze():
	pass
```
Then we started inspecting the model. Looking around in the parameters of the model we found a matrix called `maze` containing only 1s, 0s, and the number 2,3 one time only. We quickly understood that the matrix was indeed a maze, starting from the point 2, ending in 3 with ones being the walls. We wrote a simple script to find the shortest path and after a few attempts we understood the flag format (a sequence of WASD for every move, hashed)
```
DSSSSSSSSDSSDDDWDDWDWDWDWWAWAWAWWDDSDSDDWWDDDSSSDDDDSDDDWDWDWWDDSSSSDDSSDDWDWWWWDWDDDSSDSDDWWWDDSSSSSAASAASASSASAAWWAAASASSSASSSSAAWAWAWWDWWWWWWAASSSSASSASAASASASSASSDSDSSAASASSAASSSSASSAAAWWAWWWDWWAWWDWDWWWDWWAAASAAASSSAAASSSSDSSSSASSSSDSDSSSSSDDWWWWWDDDDSDSSAASSDDDDSDDDDWWWWWWAWAAWWDWWWDWDWDWDWDWDWWAWWAWWDWDDSDSSDDSDDSDSSASAASASSASASSASASSSSSDDSSDDSDSDDDDDWWAWWWWAWWWAWWWDDDWWDDWWWDWWDWWDDSSDDDSSDDSSSASASSASASASSSSSDSDSDDSDSD
```
```
689bc7711b6becd9c1d92ae3bb9e5e59
```

