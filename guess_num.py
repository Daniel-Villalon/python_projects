import random


n = 10
l = [i for i in range(1, n+1)]
pick = random.choice(l)


def guessNumber(n):
  
  left = 1
  right = n 
  while left <= right:
    midpoint = (left + right) // 2  
    if guess(midpoint) == -1: #num > pick
        right = midpoint - 1
    elif guess(midpoint) == 1: #num < pick
        left = midpoint + 1
    else:
      return midpoint
    

def guess(num):
  
 
  if num > pick:
    return -1
  if num < pick:
    return 1
  if num == pick:
    return 0 
  
   



        
print(guessNumber(n))