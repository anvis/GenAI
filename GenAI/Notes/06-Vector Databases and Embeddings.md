
**What are Vector Databases?**

A vector database is a specialized database designed to store and search data.
Here Data is represented as vectors (numerical representations). 
These databases are optimized for similarity search, allowing users to find data points that are close to a given query vector. 
They are crucial for applications like AI, semantic search, and recommendation systems. 

**Similarity Search**:

“Similarity search” or “semantic search” refers to finding information that has similar features or meaning from a set of data. It’s like searching for similar movies in an app, looking for similar shoes on an e-commerce website, or finding data related to a specific meaning.

Vector databases use algorithms like Approximate Nearest Neighbor (ANN) search to quickly find similar vectors in the database. This allows for efficient retrieval of relevant data based on similarity. 

similarity search involves three main aspects: creating vector embeddings, calculating similarity, and optimizing search.

As per our code in Text Model, we create Embeddings from LLM and store them in the Vector DB, when query is passed we do similar search on vector db and pass on the result to LLM Model as Documents. The LLM then will give us the required output.


**Vector Representation:**

Data is converted into numerical vectors (arrays of numbers) that capture its characteristics.
For example, text can be represented as a vector based on word frequencies, and images can be represented based on pixel values or feature extraction. 

A vector is essentially a list of numbers that represent some properties of the data. These numbers are placed in a specific order, forming a multidimensional space where relationships between data points can be analyzed.

- **Text Representation (Word Embeddings)**:

Words can be converted into numerical vectors using models like Word2Vec, GloVe, or FastText. The idea is that words with similar meanings will have similar numerical representations, allowing computers to understand language in context.
  
- **Image Representation**:

Pixels of an image can be represented in a multi-dimensional space where each pixel’s color (Red, Green, Blue values) forms a vector.

![image](https://github.com/user-attachments/assets/ec77177b-a0fd-4ff3-9f86-f50b12243e52)

In this space, "King" and "Queen" have similar vector values, indicating their relationship. Likewise, "Man" and "Woman" share similarities. 

The important aspect of generated embeddings is that similar or semantically related data tend to be located closer to each other, while dissimilar data are located farther apart. This is because AI models are trained on data that helps them identify meanings, similarities, and differences.

![image](https://github.com/user-attachments/assets/110ca8d6-d413-4d53-97d5-09c8607d8512)

![image](https://github.com/user-attachments/assets/8828385a-d50a-4462-b6f7-fc9606ccedd6)


**Calculating similarity**

Now that we understand how data is represented, we can learn how to find relevant results by calculating the distances between the vector representation of the search query and the existing data.

To find potentially similar data vectors to a query vector, we calculate the distance between all data vectors and the query vector.

However, not all data is relevant. Therefore, we only need the data vectors that are closest to the query vector, as they are potentially similar. 
To improve accuracy, we can limit the number of closest vectors to a certain count. 
When performing a search, the additional information of count or top “K” is provided, which represents the number of closest vectors.

![image](https://github.com/user-attachments/assets/54276fc3-d470-4963-bf64-68fc1353de84)

**optimizing search**

There are multiple ways to optimize your search, detailed description is given below.
https://medium.com/@sudhiryelikar/understanding-similarity-or-semantic-search-and-vector-databases-5f9a5ba98acb



**Vector Databases**: Purpose and importance in generative AI applications.
*   **Embeddings**: Numerical representations with semantic meaning (vectors).
*   **Similarity Search**: Using embeddings to find similar information.
*   **Widely Used Vector Databases**:
    *   **Pinecone**: Setup, API key generation, index creation, clusters, storing embeddings, similarity search.
    *   **Chroma DB**: Installation and basic usage for storing and retrieving embeddings.
    *   **FAISS (Facebook AI Similarity Search)**: Mentioned as another vector database.
*   **Embedding Techniques**: Word2Vec (brief introduction to the concept of creating feature vectors).
*   **Semantic Indexing**: Building clusters based on vector distances.



FAISS and ChromaDB are both vector databases designed for efficient similarity search, but they have distinct strengths depending on your use case.

### **FAISS (Facebook AI Similarity Search)**
- **Optimized for speed**: FAISS is highly efficient, especially for large-scale datasets, leveraging GPU acceleration for fast retrieval.
- **Scalability**: Can handle billions of vectors, making it ideal for enterprise-level applications.
- **Indexing flexibility**: Offers various indexing methods, allowing users to choose the best approach for their needs.
- **Low memory footprint**: Uses compression techniques to optimize storage.

### **ChromaDB**
- **Designed for AI applications**: ChromaDB is tailored for storing and querying embeddings, making it a great choice for LLM-based workflows.
- **In-memory storage**: Ensures fast access to data without disk latency.
- **Simple API**: Provides an easy-to-use interface for seamless integration.
- **Scalability**: Can expand efficiently as datasets grow.

### **Which One Should You Choose?**
- If you need **high-speed, large-scale similarity search**, FAISS is the better choice.
- If you're working with **LLM applications and need an easy-to-use, AI-focused vector database**, ChromaDB is more suitable.

You can find a detailed comparison [here](https://myscale.com/blog/faiss-vs-chroma-vector-storage-battle/) and [here](https://risingwave.com/blog/chroma-db-vs-pinecone-vs-faiss-vector-database-showdown/). Let me know if you need help integrating either into your workflow! 🚀
