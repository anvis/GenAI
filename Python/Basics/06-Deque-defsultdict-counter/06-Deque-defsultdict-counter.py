from collections import defaultdict

# Grouping items by their first letter
words = ['apple', 'banana', 'cherry', 'butter', 'date', 'ape','elderberry', 'fig', 'grape']
grouped_words = defaultdict(list)
for word in words:
    grouped_words[word[0]].append(word)
print(grouped_words) 

# Counting occurrences of characters in a string
char_count = defaultdict(int)
for char in 'mississippi':
    char_count[char] += 1
print(char_count) 

print("----")

from collections import defaultdict

dd = defaultdict(list)
dd['fruits'].append('apple')  # No KeyError, auto-creates empty list

print(dd)  # defaultdict(<class 'list'>, {'fruits': ['apple']})
print(dd['vegetables'])  # No KeyError, returns empty list
print(dd)  # defaultdict(<class 'list'>, {'fruits': ['apple'], 'vegetables': []})


dd_int = defaultdict(int)
dd_int['count'] += 1          # Starts at 0

print(dd_int)  # defaultdict(<class 'int'>, {'count': 1})
print(dd_int['missing'])  # No KeyError, returns 0


print("----deque----")

from collections import deque

dq = deque([1, 2, 3])
print(dq)  # deque([1, 2, 3])
dq.append(4)         # Add to right
print(dq) 
dq.appendleft(0)     # Add to left
print(dq) 
dq.pop()             # Remove from right
print(dq) 
dq.popleft()         # Remove from left
print(dq) 

print("----deque with more operations----")
dq.rotate() # Rotate right by 1
print(dq)  
dq.extend([5, 6])    # Add multiple elements to the right
print(dq)  
dq.rotate()
print(dq)
dq.extendleft([-1, -2])  # Add multiple elements to the left (reversed order)
print(dq)  
dq.rotate(-2)  # Rotate left by 2
print(dq)  # Final state of deque
dq.rotate(3)  # Rotate right by 3
print(dq)  # Final state of deque after another rotation