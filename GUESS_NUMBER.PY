import random 
def guess(x):
  random_num = random.randint(1, x)
  guess = 0 

  while guess != random_num:
    guess = int(input(f'guess a number from 1 to {x}: '))
    if guess < random_num:
      print('guess was too low')
    if guess > random_num:
      print('guess was too high')
  print(f"yay you guess the correct number:{random_num} ")


guess(5)