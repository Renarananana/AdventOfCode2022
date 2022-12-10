f = open("inputDay1")
elfString = f.read()
elfList = elfString.split("\n\n")
max_calories = 0
calories_list = []
for elf in elfList:
	elf_snacks = elf.split("\n")
	total_calories = 0
	for snack in elf_snacks:
		if snack != '':
			total_calories += int(snack)
			calories_list.append(total_calories)
	calories_list.sort()

	max_calories = max(total_calories, max_calories)
print(calories_list[-1], calories_list[-2], calories_list[-3])
print(calories_list[-1] + calories_list[-2] + calories_list[-3])