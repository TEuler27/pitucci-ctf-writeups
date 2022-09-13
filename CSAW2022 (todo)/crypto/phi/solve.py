from sage.all import *
from Crypto.Util.number import *
from pwn import *
import owiener

def n_from_phi(phi, n):
	if phi > n:
		return False
	a = 1
	b = n - phi + 1 
	c = n

	delta = b**2 - 4*a*c
	log.info(f'{delta = }')
	dt = pow(delta, 0.5)

	if int(dt) ** 2 != delta:
		return False

	p = (-b + dt)/(2*a)
	q = (-b - dt)/(2*a)

	p = int(p)
	q = int(q)
	if n % p == 0:
		return p
	if n % q == 0:
		return q

	return False


flags = ['d0nt_reUs3_c0mm0n_m0duLus_iN_RSA']
# flag{aR3nT_U_tH3_RSA_ninJA}

ns = {}
r = remote('crypto.chal.csaw.io', 5000)
lines = r.recvuntil(b'\n>').decode() 
r.sendline(b'solve_challenge d0nt_reUs3_c0mm0n_m0duLus_iN_RSA')
r.recvuntil(b'flag')

# Recover phi from e and d heuristic ??????
ns = {}
j = 0
while True:
	log.info(f'{j = } {len(ns) = }')
	lines = r.recvrepeat(1.5).decode().strip().split('\n')
	dic = {}
	for l in lines:
		if l.strip() == '':
			continue
		if not ('N =' in l or 'e =' in l or 'd =' in l):
			break
		u = l.split('=')
		dic[u[0].strip()] = int(u[1].strip())
	#log.info(f'{dic = }')

	n = dic['N']
	e = dic['e']
	d = dic['d']
	guess = e*d - 1

	if n in ns:
		phi = gcd(ns[n], guess)
		old_phi = ns[n]
		print(f'{len(str(phi)) = } {len(str(old_phi)) = }')
		msg = f'phi {phi}'
		r.sendline(msg.encode())
		lines = r.recvrepeat(2).decode()
		log.info(lines)
		ns[n] = phi
		"""
		phi = gcd(ns[n] + [guess])
		log.info(f'Guessing {phi = }')
		log.info(f'Ratio {n // phi = }')
		for i in range (1,6):
			p = n_from_phi(i*phi, n)
			if p:
				q = n // p
				log.info(f'old {i*phi = } ')
				phi = (p-1)*(q-1)
				log.info(f'new {phi = } ')
				
				msg = f'phi {phi}'
				r.sendline(msg.encode())
				lines = r.recvrepeat(2).decode()
				log.info(lines)
			else:
				log.info(f'Fail find phi {i = }')
		ns[n] += [guess]
		log.info(f'{len(ns[n]) = }')
		"""

	else:
		ns[n] = guess

	r.sendline(b'1')
	j += 1



""" COMMON MODULUS ATTACK
for j in range(20):
	log.info(f'{j = }')
	
	r.sendline(b'1')
	lines = r.recvrepeat(1).decode().strip().split('\n')
	
	dic = {}
	for l in lines:
		if not ('N =' in l or 'e =' in l or 'c =' in l):
			break
		u = l.split('=')
		dic[u[0].strip()] = u[1].strip()

	if 'N' in dic:
		n = int(dic['N'])
		e = int(dic['e'])
		c = int(dic['c'])

		if n in ns:
			#log.info(f'{ns[n] = }')
			e1, c1 = e, c
			e2, c2 = ns[n][0]

			_, x, y = xgcd(e1, e2)
			if _ != 1:
				log.info(f'{e1 = } {e2 = } Fail')
				continue
			log.info(f'{x = } {y = }')
			
			m = (pow(c1, x, n) * pow(c2, y, n))%n

			#cc2 = pow(c2, -1, n)
			#m1 = pow(c1, x, n)
			#m2 = pow(c2, -y, n)
			#m = (m1*m2) % n
			log.info(f'{m = }')
			m = long_to_bytes(int(m))
			log.success(f'{m = }')
		
		else:
			ns[n] = [(e,c)]


	#r.close()
	log.info(f'{len(ns) = }')
"""