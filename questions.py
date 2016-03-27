quiz = [
{'question': '1. Which word describes you better?', 'answers': [{'response': 'a.fearless', 'movie': 'thriller'}, {'response': 'b.witty', 'movie': 'comedy'},{'response': 'c.sensible', 'movie': 'drama'},{'response': 'd.determined', 'movie': 'action'},{'response': 'e.passionate', 'movie': 'romance'}]},
{'question':'2.Which aspect of a movie is the most important one?','answers': [{'response': 'a.plot twists', 'movie': 'thriller'}, {'response': 'b.powerful emotions', 'movie': 'romance'},{'response': 'c.jokes', 'movie': 'comedy'},{'response': 'd.suspense', 'movie': 'action'}]},
{'question':'3. Who is the best hero?','answers': [{'response': 'a.Homer Simpson', 'movie': 'comedy'}, {'response': 'b.Jack(Titanic)', 'movie': 'romance'},{'response': 'c.Augustus Waters', 'movie': 'drama'},{'response': 'd.Princess Leia', 'movie': 'action'},{'response': 'e.Rambo', 'movie': 'thriller'}]},
{'question':'4. What\'s the best time to watch a movie?','answers': [{'response': 'a.at sunset/sunrise', 'movie': 'drama'}, {'response': 'b.anytime', 'movie': 'comedy'},{'response': 'c.afternoon', 'movie': 'action'},{'response': 'd.2 AM', 'movie': 'thriller'}]},
{'question':'5. Which of these movies appeals more to you?','answers': [{'response': 'a.The Notebook', 'movie': 'romance'}, {'response': 'b.Titanic', 'movie': 'drama'},{'response': 'c.Star Wars', 'movie': 'action'},{'response': 'd.The Nightmare on Elm Street', 'movie': 'thriller'},{'response': 'e.American Pie', 'movie': 'comedy'}]},
{'question':'6. If you could visit any of these places, which one would you choose?','answers': [{'response': 'a.Paris', 'movie': 'romance'}, {'response': 'b.Las Vegas', 'movie': 'comedy'},{'response': 'c.A haunted mansion', 'movie': 'thriller'},{'response': 'd.Sicily', 'movie': 'action'}]},
{'question':'7. What kind of dreams do you have?','answers': [{'response': 'a.Fighting', 'movie': 'action'}, {'response': 'b.Partying', 'movie': 'comedy'},{'response': 'c.Being on a date', 'movie': 'romance'},{'response': 'd.Running', 'movie': 'thriller'}]},
{'question':'8. Do you like a happy ending?','answers': [{'response': 'a.Yes', 'movie': 'comedy'}, {'response': 'b.No', 'movie': 'thriller'}]},
{'question':'9. How does your average movie night look like?','answers': [{'response': 'a.Having a good laugh', 'movie': 'comedy'}, {'response': 'b.Alone with tissues', 'movie': 'drama'},{'response': 'c.Day-dreaming', 'movie': 'romance'},{'response': 'd.Enjoying something high-energy', 'movie': 'action'},{'response': 'e.Trying to scare myself', 'movie': 'thriller'}]},
{'question':'10. What\'s your favorite color?','answers': [{'response': 'a.pink', 'movie': 'romance'}, {'response': 'b.black', 'movie': 'thriller'},{'response': 'c.red', 'movie': 'action'},{'response': 'd.light purple', 'movie': 'drama'},{'response': 'e.blue', 'movie': 'comedy'}]}
]



for question in quiz:
    long_question = question['question']+"\n"
    for possible_answer in question['answers']:
    	long_question += possible_answer['response'] + "\n"
    answer = int(input(long_question))
    print ("I think you would like "+  question['answers'][answer]['movie'] + " movies")
