import base64 as b64
from pwn import *
import datetime

def fixed_xor(a: bytes, b:bytes) -> bytes:
	return bytes(x^y for x,y in zip(a,b))

def bytes_to_chunks(b: bytes, chunk_size: int = 16) -> list:
	chunks = [b[i:chunk_size+i] for i in range(0, len(b), chunk_size)]
	return chunks

def enc(a1: bytes, a2: bytes, r: remote) -> bytes:
	r.recvuntil(b'\n>')
	r.sendline(b'1')
	r.recvuntil(b'\n>')
	r.sendline(a1)
	r.recvuntil(b'\n>')
	r.sendline(a2)
	r.recvline()

	cip_iv = r.recvline().decode()
	cip_iv = cip_iv.split("'")[1].split(':')[1].strip()
	return cip_iv

def dec(enc: bytes, r: remote):
	# enc è b64encoded

	r.recvuntil(b'\n>')
	r.sendline(b'2')
	r.recvuntil(b'\n>')
	r.sendline(enc)
	
	r1 = r.recvline().decode()
	if 'Try again' in r1 or 'Valid plaintext' in r1:
		res = r1
	else:
		res = r.recvline().decode()
	
	if 'Enter your' in res:
		log.info(f'Error \n{enc = } \n{r1 = }\n{res = }')
		r2 = r.recvuntil(b'\n>')
		log.info(f'{r2 = }')
		r.sendline(b'2')
		r2 = r.recvuntil(b'\n>')
		log.info(f'{r3 = }')
		r.sendline(enc)		
		r4 = r.recvline()
		log.info(f'{r4 = }')
		res = r.recvline().decode()
		log.info(f'{res = }')

	if 'Valid plaintext.' in res:
		return 42
	else:
		return 0

	# Check for outcome
	#log.info(f'{res = }')
	return res

def single_block_attack(ct: bytes, true_iv: bytes, r: remote) -> bytes:
	# ct = iv + true_ct + fake_block
	# se true_ct ha lunghezza piena (dovrei poterlo sempre fare)
	# allora il messaggio è valido solo se l'ulitmo byte di fake block diventa 32

	# plain = 32^v^i
	ascii_text_chars = list(range(32, 127))

	log.info(f'{true_iv = } {true_iv[-1] = }')
	blocks = bytes_to_chunks(ct)
		
	for candidate in range(256):
		expected = 32 ^ true_iv[-1] ^ candidate
		if not expected in ascii_text_chars:
			continue

		expected = expected.to_bytes(1, byteorder='big')


		new_block = [0] * 16
		new_block[-1] = candidate
		new_block = bytes(new_block)
		blocks[-2] = new_block
		
		msg = b64.b64encode(b''.join(blocks))
		#log.info(f'{msg = }')
		log.info(f'{candidate = } {expected = }')
		res = dec(msg,r)
		if res == 42:
			log.success(f'Byte found: {expected}')
			return expected


def full_attack(r: remote):
	# Voglio che il mio target byte sia in fondo a un chunk
	# Il primo blocco sono 90 caratteri + le a quindi il primo byte della flag è 90
	# In tutto le a devono essere 11 mod 16 per far apparire il blocco di pad
	
	flg = b'flag{poodle_atk'
	while True:
		target_byte = 90 + len(flg)
		n1 = 0
		while (target_byte + n1 + 1) % 16 != 0:
			n1 += 1
		n2 = 0
		while (n1 + n2) % 16 != 11:
			n2 += 1

		target_block = (target_byte + n1 + 1)//16
		iv_block = target_block - 1

		log.info(f'{flg = } Recovered: {len(flg)}/22 {target_byte = } {n1 = } {n2 = } {target_block = } {iv_block = }')

		a1 = n1 * b'a'
		a2 = n2 * b'a'

		cip = enc(a1, a2, r)
		cip = b64.b64decode(cip)

		blocks = bytes_to_chunks(cip)
		blocks.append(blocks[target_block])
		cip = b''.join(blocks)

		flag_char = single_block_attack(cip, blocks[iv_block], r)
		flg += flag_char
		log.info(f'{target_byte = } {flag_char = }')
		log.info(f'{flg = }')


if __name__ == '__main__':
	log.info('Starting attack')
	r = remote('crypto.chal.csaw.io', '5004')

	#msg = b"Congratulations, you just completed your " + b"a" + b" purchase instead of buying this beautiful flag: "
	#msg += b". What were you thinking? Fortunately you have helped " + b"a" + b" canines and puppies find homes"
	#log.info(f'{len(msg) = }')



	full_attack(r)

	# Passo il secondo blocco, true iv è il primo
	


	#cip = b64.b64decode(cip_iv)
	#blocks = bytes_to_chunks(cip)
	#single_block_attack(blocks[1], blocks[0], r)

	
	# Sanity check
	"""
	r.recvuntil(b'\n>')
	r.sendline(b'2')
	r.recvuntil(b'\n>')
	r.sendline(cip_iv.encode())
	r.recvline()
	res = r.recvline().decode()
	log.info(f'{res = }')
	"""