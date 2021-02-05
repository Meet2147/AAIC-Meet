QuestionNumber = 0

def fetchData():
    request = requests.get("https://opentdb.com/api.php?amount=15&category=9&difficulty=medium&type=multiple")
    request_text = request.text
    data = json.loads(request_text)
    if data is None:
        print("Error, server connection failed")
    else:
        return data['results']
    
questions = fetchData()

def getQuestions():
    list = []

    for question in questions:
        list.append(question['question'])
        list.append(question['correct_answer'])
        for incorrectAnswer in question['incorrect_answers']:
            list.append(incorrectAnswer)

    return list
        

questionList = getQuestions()
