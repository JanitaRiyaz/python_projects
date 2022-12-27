quiz={
    "question1":{
        "question":"What is the capital of Pakistan? ",
        "answer":"Islambad"

    },
    "question2":{
        "question":'what is the capital of India? ',
        "answer":"Dehli"

    },
    "question3":{
        "question":"What is the capital of iran",
        "answer":"Sheraz"
    },
    "question4":{
        "question":"What is the capital of France? ",
        "answer":"Rome"

    },
    "question5":{
        "question":"What is the capital of Germany",
        'answer':"Berlin"
    },
    "question6":{
        "question":"what is the capital of italy",
        "answer":"Rome"
    }

}
score=0


for key,value in quiz.items():
    print(value['question'])
    answer=input("Answer: ")
    if answer.lower()==value['answer'].lower():
        score=score+1
        print("your score is " + str(score))
        print('Your answer is correct')
       
        print("")
       
       
    else:
        print('Your answer is incorrect')
        print('Correct answe is'+ value['answer'])
        print(f"your score is {score}")
        print("")
print(f'You got {score} answes right out if 6')
print(f"your percentage is {score/6*100} ")