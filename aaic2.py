import json
import random

chk = random.randint(0, 4)
count = 0
total = 1

with open("q.json", "r+") as f:
	data = json.load(f)

def json_convert():
	lst1 = list()
	for i in data["sport"]:
		lst1.append(i)
		return lst1


def json_fetch():
	choice = int(input('ENTER YOUR CHOICE: '))
	global chk, count
	lst = json_convert()
	dic = lst[0]
	lst1 =list()
	lst1.append(dic["question"])
	for j in(dic["options"]):
		lst1.append(j)
	lst1.append(dic["answer"])
	chk +=2
	count +=1
	return lst1


if __name__ == "__main__":
	choice = 1
	while choice != 3:
		print('\n=========WELCOME TO AAIC QUIZ==========')
		print('----------Developer: MEET JETHWA----------')
		print('1. Sport')
		print('2. Math')
		print('3. History')
		print('4. Exit')

		if choice == 1:
			json_fetch()
			break









	



