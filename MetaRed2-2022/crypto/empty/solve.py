from pwn import xor

with open('empty.pdf', 'rb') as fh:
	enc = fh.read().strip()

magic = b'%PDF-'
start = enc[:20]

key = b'\x16'
out = xor(key, enc)
with open('flag.pdf', 'wb') as fh:
	fh.write(out)

# CTFUA{16_8s_a_mag8c_number}