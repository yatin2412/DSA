a = [int(i) for i in input().split()]
for i in range(len(a)):
	min_index = i
	for j in range(i+1,len(a)):
		if a[j]<a[min_index]:
			min_index = j
	if min_index == i:
		continue
	else:
		a[i],a[min_index] = a[min_index],a[i]
print(a)