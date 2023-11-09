cardStack = []

cardStack.append('Jack of Hearts')
cardStack.append('2 of Diamonds')
cardStack.append('10 of Spades')

#it is just a list, but limiting our operations on it (to pop and push) it can be a stack

topCard = cardStack.pop()
print(topCard)
topCard = cardStack[-1]
print(topCard)

if not cardStack:
  print('card stack is empty')
else:
  print(len(cardStack))