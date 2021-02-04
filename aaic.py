import json 

import random



def sport():
	score = 0
	print("Sports Selected")
	with open("quiz.json", "r+") as f:
		j = json.load(f)["quiz"]["sport"]
		for i in range(len(j)):
			no_of_questions = len(j)

			ch = random.randint(0, no_of_questions)
			print(f'\nQ{i+1}) {j[list(j.keys())[ch]]["question"]}\n')
			for option in j[list(j.keys())[ch]]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[list(j.keys())[ch]]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[list(j.keys())[ch]]
		print(f'\nFINAL SCORE: {score}')

def maths():
	score = 0
	print("Maths Selected")
	with open("quiz.json", "r+") as f:
		j = json.load(f)["quiz"]["maths"]
		for i in range(len(j)):
			no_of_questions = len(j)
			if no_of_questions == 0:
				break
			ch = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1}) {j[list(j.keys())[ch]]["question"]}\n')
			for option in j[list(j.keys())[ch]]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if j[list(j.keys())[ch]]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del j[list(j.keys())[ch]]
		print(f'\nFINAL SCORE: {score}')
	

	
		

if __name__ == "__main__":
	choice = 1
	while choice != 3:
		print('\n=========WELCOME TO AAIC QUIZ==========')
		print('----------Developer: MEET JETHWA----------')
		print('1. Sport')
		print('2. Math')
		print('3. Exit')
		
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			sport()
			break
		elif choice == 2:
			maths()
			break
		elif choice == 3:
			break
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')






