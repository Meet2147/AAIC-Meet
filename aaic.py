import json 

import random
choice = 1
def question(cat, j):
	score = 0


	print(cat,"Selected")

	for i in range(len(j)):
		no_of_questions = len(j)



		ch = random.randint(0, no_of_questions-1)
		print(f'\nQ{i + 1}) {j[list(j.keys())[ch]]["question"]}\n')
		for option in j[list(j.keys())[ch]]["options"]:
			print(option)
		answer = input("\nEnter your answer: ")
		if j[list(j.keys())[ch]]["answer"][0] == answer[0].upper():
			print("\nYou are correct")
			score += 1
		else:
			print("\nYou are incorrect")
		del j[list(j.keys())[ch]]
	print(f'\nFINAL SCORE: {score}')



if __name__ == "__main__":


	with open('quiz.json', 'r+') as f:
		j = json.load(f)['quiz']
	jcat = {str(i + 1): x for i, x in enumerate(j.keys())}



	print('\n=========WELCOME TO AAIC QUIZ==========')
	print('----------Developer: MEET JETHWA----------')
	for each in jcat.keys():
		print(each, jcat[each])

	choice = input('ENTER YOUR CHOICE: ')
	question(jcat[choice],j[jcat[choice]])












