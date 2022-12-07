f = open("inputDay3", "r")
input_ = f.read()
backpacks =input_.split("\n")
sum_priorities = 0
for group in range(0,len(backpacks)-1, 3):
	a = backpacks[group]
	b = backpacks[group + 1]
	c = backpacks[group + 2]
	items_a = [item for item in a]
	items_b = [item for item in b]
	items_c = [item for item in c]
	items_a.sort()
	items_b.sort()
	items_c.sort()
	i = 0
	j = 0
	repeted = []
	while i < len(a) and j < len(b):
		if items_a[i] == items_b[j]:
			repeted.append(items_a[i])
			i += 1
			j += 1
		elif items_a[i] < items_b[j]:
			i += 1
		else:
			j += 1
	i = 0
	j = 0
	repeted_3 = ''
	while i < len(c) and j < len(repeted):
		if items_c[i] == repeted[j]:
			repeted_3 = items_c[i]
			break
		elif items_c[i] < repeted[j]:
			i += 1
		else:
			j += 1
	if repeted_3 <= 'z' and repeted_3 >= 'a':
		sum_priorities += ord(repeted_3)- ord('a') + 1
	elif repeted_3 <= 'Z' and repeted_3 >= 'A':
		sum_priorities += ord(repeted_3)- ord('A') + 27
	else:
		print("error")
print(sum_priorities)
