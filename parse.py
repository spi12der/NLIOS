import subprocess as sp
for i in range(0,10):
	print i

tmp = sp.call('clear',shell=True)

for i in range(11,20):
	print i