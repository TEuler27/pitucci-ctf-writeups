with open('secret', 'rb') as fh:
	data = fh.read().strip()


data = list(data)
data[0] = 137 
data[1] = 80 
data[2] = 78 
data[3] = 71

with open('secret.png', 'wb') as fh:
	fh.write(bytes(data))

