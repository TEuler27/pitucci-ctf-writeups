a = 'CT0N_2TR2_T4F411HFUNT243A21NT}{P0T_'
out = ''

for i in range(6):
	for j in range(len(a)):
		if j%6 == i:
			out += a[j]

print(out)
# CTFUA{TR4N2P021T10N_12NT_TH4T_24F3}