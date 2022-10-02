x = 0
y = 0
print( "!0! !" ,end='')
for i in range(25):
	if x == 0:
		x = 1
	else:
		z = x
		x = x + y
		y = z
	if i != 24:
		print(x, end="! !")
	else:
		print(x, end="!")	