
🔁 deque: Double-Ended Queue
- Purpose: Optimized for fast appends and pops from both ends.
- Use Case: Ideal for implementing queues, stacks, or sliding windows.
-  Supports rotation (dq.rotate(n)) and max length (deque(iterable, maxlen)).

---

🧩 defaultdict: Dictionary with Default Factory
- Purpose: Automatically creates default values for missing keys.
- Use Case: Great for grouping, counting, or building nested structures.

defaultdict is a subclass of dict that provides a default value for a nonexistent key, avoiding KeyError.
It requires a callable (like list, int, or a custom function) to initialize the default value.

``` python
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

Output:
defaultdict(<class 'list'>, {'a': ['apple', 'ape'], 'b': ['banana', 'butter'], 'c': ['cherry'],
'd': ['date'], 'e': ['elderberry'], 'f': ['fig'], 'g': ['grape']})
defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
```

``` python

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

Output:

defaultdict(<class 'list'>, {'fruits': ['apple']})
[]
defaultdict(<class 'list'>, {'fruits': ['apple'], 'vegetables': []})
defaultdict(<class 'int'>, {'count': 1})
0

```


---

🔢 Counter: Frequency Tally
- Purpose: Counts occurrences of hashable items.
- Use Case: Perfect for NLP token frequency, histogram generation, or voting systems.

Counter is a subclass of dict designed for counting hashable objects. 
It stores elements as dictionary keys and their counts as dictionary values.
This makes it particularly useful for tallying occurrences of items in an iterable.

``` python

from collections import Counter

# Counting occurrences of words in a list
words = ['red', 'blue', 'red', 'green', 'blue', 'blue']
word_count = Counter(words)
print(word_count) # Output: Counter({'blue': 3, 'red': 2, 'green': 1})

# Finding the most common elements
most_common_words = word_count.most_common(2)
print(most_common_words) # Output: [('blue', 3), ('red', 2)]

```
