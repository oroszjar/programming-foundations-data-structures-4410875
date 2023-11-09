from collections import deque

history_stack = deque()

history_stack.append('https://www.google.com/')
history_stack.append('https://www.linkedin.com/')
history_stack.append('https://stackoverflow.com/')

print(history_stack[-1])
print(history_stack.pop())

