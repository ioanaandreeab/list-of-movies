score = {
    'romance': 0,
    'thriller': 0,
    'comedy': 0,
    'drama': 0,
    'action': 0
}

import json

with open("C:/Users/Andreea/Desktop/quiz.json") as json_file:
    quiz = json.load(json_file)
    


for question in quiz:
    long_question = question['question']+"\n"
    for possible_answer in question['answers']:
        long_question += possible_answer['response'] + "\n"
    answer = input(long_question)
    for possible_answer in question['answers']:
        if possible_answer['response'].startswith(answer):
            movie = possible_answer['movie']
            score[movie] = score[movie] + 1
print (score)
