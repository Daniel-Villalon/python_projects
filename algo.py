def binary(list, target):
  if len(list) < 0:
    return list 
  
  left = 0 
  right = len(list) - 1 
 
  while left <= right:
    midpoint = (left + right) // 2

    if list[midpoint] == target:
      return midpoint
    if list[midpoint] < target:
      left = midpoint + 1 
    else:
      right = midpoint - 1

  return None 




l = [1, 2, 3, 6, 7, 9, 10, 34, 55]

target = 1

print(binary(l, target))