import numpy as np
from pwn import *
from sympy import Poly, ZZ
from sympy.abc import x
import sympy

x = sympy.Symbol('x')

r = remote('crypto.chal.csaw.io', 5003)
r.recvuntil(b'\n>')
r.sendline(b'1')
lines = r.recvuntil(b')').decode()

cip = lines.split('(')[1].split(',')[0]
cip = sympy.polys.polytools.poly_from_expr(cip)[0]
#log.info('Got cip')

r.recvuntil(b'\n>')
r.sendline(b'2')
lines = r.recvuntil(b')').decode()

key = lines.split('(')[1].split(',')[0]
key = sympy.polys.polytools.poly_from_expr(key)[0]
#log.info('Got key')

plain = cip - key
log.info(f'{plain = }')
log.info(f'{plain.all_coeffs() = }')

input_arr = plain.all_coeffs()
output = np.packbits(np.array(input_arr).astype(int)).tobytes()
log.info(f'{output = }')

input_arr.reverse()
log.info(f'{input_arr = }')
output = np.packbits(np.array(input_arr).astype(int)).tobytes()
log.info(f'{output = }')
