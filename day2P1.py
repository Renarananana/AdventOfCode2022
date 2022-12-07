f = open("inputDay2p1", "r")
input_ = f.read()
rounds =input_.split("\n")
points = 0
for round_ in rounds[:-1]:
	plays = round_.split(" ")
	if plays[1] == "X":
		points += 1
		if plays[0] == "A":
			points += 3
		elif plays[0] == "C":
			points += 6
	elif plays[1] == "Y":
		points += 2
		if plays[0] == "B":
			points += 3
		elif plays[0] == "A":
			points += 6
	else:
		points += 3
		if plays[0] == "C":
			points += 3
		elif plays[0] == "B":
			points += 6
print(points)
l = ['d', 'c', 'b', 'a']
l2 = l[:2]
l2.sort()
print(ord('A'))