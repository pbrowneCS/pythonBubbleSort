import random
import datetime
startTime = datetime.datetime.now()
arr = []
for k in range(100):
	arr.append(random.randint(0,10000))
def selectSorting(x):
	for i in range(0,len(x)):
		temp = x[i]
		tempKey = i
		tempMin = x[i]
		tempMinKey = i
		for j in range(i+1,len(x)-i-1):
			if temp < x[j]:
				temp = x[j]
				tempKey = j
			if tempMin > x[j]:
				tempMin = x[j]
				tempMinKey = j
		(x[len(x)-i-1], x[tempMinKey]) = (x[tempMinKey], x[len(x)-i-1])
		(x[i], x[tempKey]) = (x[tempKey], x[i])
	print x
selectSorting(arr)
print "This program took", datetime.datetime.now() - startTime, "to run"
secondStartTime = datetime.datetime.now()
def selectSortingFull(x):
	for i in range(0,len(x)):
		temp = x[i]
		tempKey = i
		for j in range(i+1,len(x)):
			if temp > x[j]:
				temp = x[j]
				tempKey = j
		(x[i], x[tempKey]) = (x[tempKey], x[i])
	print x
selectSortingFull(arr)
print "This program took", datetime.datetime.now() - secondStartTime, "to run"
#first foreloop, select value to swap, and find what to swap with, then swap
#inner loop compare 
# x[i] = 5