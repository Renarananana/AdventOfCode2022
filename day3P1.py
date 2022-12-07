f = open("inputDay3", "r")
input_ = f.read()
backpacks =input_.split("\n")
sum_priorities = 0
for backpack in backpacks[:-1]:
	items = [item for item in backpack]
	n = int(len(items)/2)
	items1 = items[:n]
	items1.sort()
	items2 = items[n:]
	items2.sort()
	i = 0
	j = 0
	repeted = ''
	while i < n and j < n:
		if items1[i] == items2[j]:
			repeted = items1[i]
			break
		elif items1[i] < items2[j]:
			i += 1
		else:
			j += 1
	if repeted <= 'z' and repeted >= 'a':
		sum_priorities += ord(repeted)- ord('a') + 1
	elif repeted <= 'Z' and repeted >= 'A':
		sum_priorities += ord(repeted)- ord('A') + 27
	else:
		print("error")
print(sum_priorities)
