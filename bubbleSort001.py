import random
import datetime
startTime = datetime.datetime.now()
arr = []
for i in range(100):
	arr.append(random.randint(0,10000))

def bubbleSorting(x):
	larger = arr[0]
	for i in range(0,len(x)):
		for j in range(1,len(x)-(i)):
			if x[j] < x[j-1]:
				x[j-1], x[j] = x[j], x[j-1]
	print x
bubbleSorting(arr)

print "This program took", datetime.datetime.now() - startTime, "to run"

#randomly generate list array
#check first against next number
#if first number, swap first with next
#check next number
#repeat check
#i = 0>1
#j = 1>2>3
#arr = [6,9,5,7,4,2,3,1]