import sys

output="hello from main folder %s " % (sys.argv[1])

for i in range(10):
	print(output,end="<br>")