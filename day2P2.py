f = open("inputDay2p1", "r")
input_ = f.read()
rounds =input_.split("\n")
points = 0
for round_ in rounds[:-1]:
	plays = round_.split(" ")
	if plays[1] == "X":
		points += 0
		if plays[0] == "A":
			points += 3
		elif plays[0] == "B":
			points += 1
		else:
			points += 2
	elif plays[1] == "Y":
		points += 3
		if plays[0] == "A":
			points += 1
		elif plays[0] == "B":
			points += 2
		else:
			points += 3
	else:
		points += 6
		if plays[0] == "A":
			points += 2
		elif plays[0] == "B":
			points += 3
		else:
			points += 1
print(points)
