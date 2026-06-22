import numpy as np

documents = [
    "Python and NumPy are useful for fast numerical computing.",
    "RAG retrieves useful documents before the LLM writes an answer.",
    "Embeddings are vectors that represent meaning.",
]

doc_embedding_array = np.array([
    [0.9, 0.1, 0.2],
    [0.8, 0.9, 0.1],
    [0.7, 0.8, 0.2],
], dtype=np.float32)

query = "How does RAG search documents?"
query_embedding_array = np.array([0.85, 0.95, 0.10], dtype=np.float32)

scores = []

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Documents loaded:", len(documents))
print("Embeddings shape:", doc_embedding_array.shape)
print("Type of embeddings:", doc_embedding_array.dtype)
print("Query:", query)
print("Query shape:", query_embedding_array.shape)
print("Query type:", query_embedding_array.dtype)

print("\nCosine similarity with each document:")
for i in range(len(documents)):
    score = cosine_similarity(query_embedding_array, doc_embedding_array[i])
    print(f"Document {i + 1}: {score:.4f}")
    scores.append(score)

scores = np.array(scores)
best_index = np.argmax(scores)

print("\nAll scores:", scores)
print("Best matching document index:", best_index)
print("Best matching document:", documents[best_index])