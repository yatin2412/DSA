a = [int(i) for i in input().split()]
for i in range(1,len(a)):
	temp = a[i]
	j = i-1
	while j>=0 and temp<a[j]:
		a[j+1]=a[j]
		j = j-1
	a[j+1] = temp
print(a)