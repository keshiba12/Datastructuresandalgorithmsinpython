from ArrayStack import ArrayStack
s = ArrayStack()
s.push(5)
s.push(4)
s.push(4)
s.push(3)
s.push(2)

print(s.top())
print(s.is_empty())
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print(s.is_empty())