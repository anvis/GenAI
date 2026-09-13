Transformers read all tokens in parallel, not sequentially.
So by default, they don’t know which word came first.
That’s where positional encoding comes in — it gives each token a sense of order.

Sentence:
“The cat sat on the mat.”

Without position info, the model only sees a bag of tokens:
["The", "cat", "sat", "on", "the", "mat"] — all equal.
With positional encoding, each token gets a subtle pattern added to its vector:
The₁, cat₂, sat₃, on₄, the₅, mat₆


Now the model knows “cat” comes before “sat,” and “mat” is at the end.
You can think of positional encoding as GPS coordinates for words — it tells the model where each word sits in the sentence.

---

Self‑Attention — Who Should I Focus On?
Once every token knows its position, self‑attention lets each token look at all others and decide which ones matter most for understanding.
Example
Sentence:
“The cat sat on the mat because it was tired.”

When processing “it,” the model asks:
- “Should I pay attention to ‘mat’?” → low score
- “Should I pay attention to ‘cat’?” → high score
So “it” focuses more on “cat.”
That’s self‑attention — each word dynamically weighs others based on relevance.


---

- Tokens → Dense vectors (capture meaning)
- Add positional encoding (capture order)
- Apply self‑attention (capture relationships)
- Combine results → context‑aware understanding
