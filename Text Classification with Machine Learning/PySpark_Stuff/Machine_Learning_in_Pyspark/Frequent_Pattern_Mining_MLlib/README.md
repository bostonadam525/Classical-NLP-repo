# Frequent Pattern Mining in MLlib
* This repo goes over frequent pattern mining algorithms and techniques in PySpark.
* Some of this content was from the Udemy Course: "PySpark Essentials for Data Scientists"


## Frequent Pattern Mining
* These are Algorithms for data mining in databases. Let's break this down:

1. Frequent —> happens often
2. Pattern —> event occuring consistently
3. Mining —> looking for something that may not be obvious


## Common Applications of FP mining
1. Gene pattern recognition 
  * identify patterns in family, diseases, viruses, or genomes.
2. Audits
  * Recognize common combinations of audit findings (e.g. A and B co-occur)
3. Customer Analysis
  * Understand common purchase combinations and behaviors 
4. Fraud Detection
  * Recognize anomalies that are outstanding or outliers from more frequent patterns.
5. NLP
  * These techniques can be applied in natural language processing as well. 


## Algorithms for FP Mining in PySpark
1. **FP-growth (Frequent Pattern)**
  * Algo looks for frequent patterns efficiently.

2. **PrefixSpan**
  * Algo used for discovering sequential patterns in sequence databases.
  * However, this takes longer to run….



### 1. FP-Growth Algorithm Steps
* The reason why FP Growth is so efficient is that it’s a **divide-and-conquer approach.**
* Excellent blog post on this algorithm: [FP Growth — Frequent Pattern Generation in Data Mining with Python Implementation](https://towardsdatascience.com/fp-growth-frequent-pattern-generation-in-data-mining-with-python-implementation-244e561ab1c3)


1. Scan Database once
  * find frequent 1-itemset (single item pattern)

2. Sort frequent items in frequency descending order
  * This is called the *“F-list"*

3. Scan Database again!
  * Construct FP-Tree (frequent patern mining tree).

4. Construct conditional FP tree in sequence of reverse order of F-List-generate frequent item set.
  * Example of this approach is below, source: [FP-Growth Algorithm in Data Mining](https://medium.com/image-processing-with-python/fp-growth-algorithm-in-data-mining-e1064accf6a3)

![image](https://github.com/user-attachments/assets/08fb2faf-bfac-4df8-89e5-d3732f11e799)



### 2. PrefixSpan Algorithm Steps
* **Order is very important here**
* Not allowing algorithm to check for random assortments, **the data has to be in sequence.**
  * Input is a seqence span into a sequence database
      * Takes max pattern length as variable — maximum length of any sequential pattern. 
      * Any sequence EXCEEDING this pattern is included in results. 
  * Outputs
      * Number of sequences where this pattern occurs divided by total number of sequences in Database. 

* Example of this algorithm, source: [Prefix span Algorithm with pyspark](https://kalpanileo1996.medium.com/prefix-span-algorithm-with-pyspark-483ab3494373)

![image](https://github.com/user-attachments/assets/5a6aa805-bcec-4eca-a729-01334a8cb16d)


#### PrefixSpan Real life applications
1. DNA subsequence analysis
2. Customer Shopping sequences
3. Website usage
4. Fraud Detection

