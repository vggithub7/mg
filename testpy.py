import sys

output="hello %s" % (sys.argv[1])

for i in range(2):
	print(output,end=" ")