#tutorial

def hi(name):
	print ('Hi ' + name + '!')

def loop(girls):
	for name in girls:
		hi(name)
		print('Next')

def loop1():
	for i in range(1,6):
		print(i)

def loop2():
	print('loop2')
	sum=0
	for i in range(1,5):
		sum=sum+i
		print(sum)

#
print('Hello, Django girls!')
name = 'Lili'
girls=['Name1', 'Name2', 'Name3']
fi=5

hi(name)
loop(girls)
loop1()
loop2()

