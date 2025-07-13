

---

## 📦 1. Chunking with Pandas

Ideal for large CSVs or tabular data.

```python
import pandas as pd

for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    # Process each chunk
    print(chunk.shape)
```

- `chunksize`: Number of rows per chunk
- Use `concat()` to merge processed chunks if needed

🔗 [GeeksforGeeks guide on chunking with Pandas](https://www.geeksforgeeks.org/pandas/how-to-load-a-massive-file-as-small-chunks-in-pandas/)

---

## 🔁 2. Streaming with Native File I/O

### Text Files (Line-by-Line)

```python
with open('large_file.txt', 'r') as f:
    for line in f:
        process(line)
```

### Binary Files (Byte Chunks)

```python
def stream_file(path, chunk_size=4096):
    with open(path, 'rb') as f:
        while chunk := f.read(chunk_size):
            process(chunk)
```

🔗 [LabEx tutorial on streaming large files](https://labex.io/tutorials/python-how-to-stream-python-large-files-434797)

---

## 🧠 3. Generator-Based Streaming

Efficient for lazy evaluation and memory conservation.

```python
def read_large_file(path, chunk_size=1024):
    with open(path, 'r') as f:
        while chunk := f.read(chunk_size):
            yield chunk

for chunk in read_large_file('large_file.txt'):
    process(chunk)
```

---

## ⚙️ 4. Multiprocessing with Chunking

Parallelize processing of large files.

```python
import multiprocessing as mp
import itertools
import csv

def worker(chunk):
    return len(chunk)

def keyfunc(row):
    return row[0]  # Group by first column

with open('large_file.csv') as f:
    reader = csv.reader(f)
    chunks = itertools.groupby(reader, keyfunc)
    pool = mp.Pool()
    while True:
        groups = [list(chunk) for _, chunk in itertools.islice(chunks, 10)]
        if not groups:
            break
        results = pool.map(worker, groups)
```

🔗 [StackOverflow example for multiprocessing with chunking](https://stackoverflow.com/questions/8717179/chunking-data-from-a-large-file-for-multiprocessing)

---

## 🌐 5. Streaming Over HTTP

Using `httpx` for downloading large files:

```python
import httpx

url = "https://example.com/largefile.zip"
with httpx.stream("GET", url) as response:
    with open("largefile.zip", "wb") as f:
        for chunk in response.iter_bytes():
            f.write(chunk)
```

🔗 [httpx streaming guide](https://pytutorial.com/python-httpxstream_file-guide-stream-files/)

---

## 🧰 6. Libraries for Advanced Streaming

| Library       | Use Case                          | Highlights                          |
|---------------|-----------------------------------|-------------------------------------|
| `smart_open`  | S3, GCS, HDFS, HTTP               | Transparent compression, remote I/O |
| `aiofiles`    | Async file I/O                    | Non-blocking reads/writes           |
| `mmap`        | Memory-mapped file access         | Fast random access                  |

🔗 [Smart Open GitHub](https://github.com/piskvorky/smart_open)

---

