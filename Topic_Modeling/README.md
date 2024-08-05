# Topic Modeling in NLP
* This repo contains projects and experiments in topic modeling with various algorithms, techniques, and datasets.

## Topic Modeling 
- A repeated group of statistically significant tokens in a corpus, text data, or document.
- Statistical significance is usually defined by:
  1. Group of words frequently occuring together in sequences, n-grams, or clusters.
  2. Similar term and inverse document frequency intervals
  3. Frequently occuring together.
  4. Semantic similarity -- based on distance metrics (e.g. SentenceTransformers using cosine similarity)
 - Unsupervised Learning algorithms
 - Text mining or text analytics approaches

## Importance of Topic Modeling in NLP
- Document Categorization
- Document Summarization
- Dimensionality Reduction
- Information Retrieval
- Recommendation engines
- Dataset evaluation for RAG-LLM pipelines

## Topic Modeling Techniques
1. LDA - Latent Dirichlet Allocation
2. NNMF - Non-negative Matrix Factorization
3. LSA - Latent Semantic Allocation

### LDA - Latent Dirichlet Allocation
* General probabilistic topic model algorithm

This does 2 things:
* Finds topics from a corpus
* Annotates documents with topics

LDA Assumptions
* Documents are a mixture of topics
    * Statistical assumption: Documents are defined by a probability distributions of topics
* Topics are a mixture of words
    * Statistical assumption: Topics are defined by a probability distributions of words


How does LDA Work?
* LDA applies 2 main assumptions to the data:

1. Corpus : Document Word Matrix
2. Document Word Matrix = Document Topic Matrix + Topic Word Matrix
   * The concept is a document word matrix is equal to a **document topic matrix** + **topic word matrix**
  
What is the goal of LDA?
* Optimize representations in text.
1. Document topic distributions
2. Topic terms distributions


LDA uses an Iterative process for Topic Modeling:
1. First assigns random topics to each word - recall that documents are a mixture of topics and topics are a mixture of terms.
2. Optimization steps in LDA
   * Iterates through each document (d)
   * Iterates through each word (w)

* LDA assumes that all topic assignments except the current word are correct. 
* LDA tries to correct the **current word** using probability computations p1 and p2.
* P1 and P2 are defined as follows:

`P1 = proportion (topic t / document d)`
`P2 = proportion (word w / topic t)`

P1 —> is the proportion of words in document d that are currently assigned to topic t
P2 —> is the proportion of assignments to topic t that come from w, over all documents


Using probabilities, LDA then reassigns w of document d a new topic k’
- Where we choose topic k’ with a new probability
- = p1 * p2

These steps are repated numerous times until a "steady state" is reached where optimal matrix probabilities are obtained and the exhaustive number of topics.
