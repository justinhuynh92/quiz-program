# add a dictionary that stores questions and answers
quiz = {
    "question1": {
        "question": "What is the capital of France?"
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?"
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?"
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?"
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?"
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?"
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?"
        "answer": "Vienna"
    },
}

# have a variable that tracks the score of the player
score = 0

# loop through the dictionary using the key, values pair
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    # tell them if they are right or wrong
    if answer.lower() == value['answer'].lower():
        print('Correct')
        #increase score for each win
        score = score + 1
        print("Your score is: " + str(score))
    else:
        print('Wrong')
        print('The answer is : ' + value['answer'])
        print("Your score is: " + str(score))

# show the final result when quiz is completed
print("You got " + str(score) + " out of 7 questions correctly.")
#convert to a percentage
print("Your percentage is " + str(int(score/7 * 100)) + "%")
