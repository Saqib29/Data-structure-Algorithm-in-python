from collections import deque

history = deque()


history.appendleft('saqib')
history.appendleft('aminul')
history.appendleft('islam')

print(history)

history.popleft()
print(history)

history.popleft()
print(history)
