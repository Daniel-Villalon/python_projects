from questions import citizenship_questions
import random

def citizenship_game(questions):
  questions = list(questions.keys())
  random.shuffle(questions)

  score = 0

  while True:
    for question in questions:
      print("----------\n")
      print(f"Score = {score}\n")
      print('\n' + question + '\n')

      if type(citizenship_questions[question]) == list:
        print("ANSWER: " , ", ".join(citizenship_questions[question]) , '\n')
      else:
        print("ANSWER: " , (citizenship_questions[question]) , '\n')

      print(type(citizenship_questions[question]), '\n')      

      user_input = input("Your answer: ").lower()

      correct_answer = citizenship_questions[question]
      print(correct_answer)
      
  
      if type(correct_answer) == str:
        if user_input.lower() == correct_answer.lower():
          print("\n CORRECT!")
          score += 1

          print('\n ----------')
        else:
          print('\n WRONG!')
          print('\n ----------')
          score -= 1

      elif type(correct_answer) == list:
        if user_input.lower() in [answer.lower() for answer in correct_answer]:
          print("\n CORRECT!")
          score += 1
          print('\n ----------')
        else:
          print('\n WRONG!')
          print('\n ----------')
          score -= 1

  print('the game is finished')
     

  
citizenship_game(citizenship_questions)