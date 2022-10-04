# Get the key by xoring spi.ce and spi.txt
with open('spi.ce', 'rb') as fh:
	ce = fh.read()

with open('spi.txt', 'rb') as fh:
	txt = fh.read()

print(bytes(x^y for x,y in zip(ce,txt))) # DUN3
key = b'DUN3'

# Get flag
with open('flag.ce', 'rb') as fh:
	cip = fh.read().strip()

flag = []
state = 0
for c in cip:
	flag.append(c ^ key[state])
	state = (state+1)%4

out = bytes(flag)
with open('flag.png', 'wb') as fh:
	fh.write(out)

# CTFUA{X0R_4II_TH3_TH1NG2}