from collections import deque

def generateBinary(n):
 number_queue = deque()
 if not type(n) == int or not int(n) > 0:
  return None
 else:
  while n > 0:
    number_queue.append(bin(n))
    n-=1
  return number_queue

# input: n
# output: print first n binary numbers

print(generateBinary(5))
print(generateBinary(1))
print(generateBinary(0))
print(generateBinary(-5))
print(generateBinary('asd'))
