# Mini RAG Retriever with NumPy

This is my first beginner-friendly Mini RAG Retriever project built using Python and NumPy.

## What this project does

- Stores a small set of documents
- Stores simple document embeddings as NumPy arrays
- Stores one query embedding
- Uses cosine similarity to compare the query with each document
- Uses `np.argmax()` to find the best matching document

## Concepts used

- NumPy arrays
- array shape
- dtype
- dot product
- cosine similarity
- `np.argmax()`

## Files

- `retriever.py` → main Python file
- `README.md` → project explanation

## How to run

```bash
python retriever.py
```

## Example output

The program prints:
- similarity score for each document
- all scores as a NumPy array
- the best matching document

## Why this project matters

This project is a tiny beginner version of the retrieval part of RAG systems.
It helped me practice NumPy basics and understand how vector-based search works.