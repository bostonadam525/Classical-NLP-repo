# PySpark Stuff
* This repo is everything related to big data processing in PySpark.
* See PySpark docs: https://spark.apache.org/docs/latest/api/python/index.html


# Speed of PySpark
* Run workloads 100x faster
* Uses state of the art DAG scheduler, query optimizer and physical execution engine.
* Apache Spark is 100x faster than Map Reduce.
* Key points about Spark's speed advantages:
  * 1. **In-memory processing**
    * Spark stores intermediate data in RAM, allowing for much faster data access compared to disk-based MapReduce. 
  * 2. **Optimized for iterative tasks**
    * Spark is designed to efficiently handle iterative algorithms where data needs to be accessed multiple times, further enhancing performance. 
  * 3. **Improved parallelism**
  * Spark can effectively distribute tasks across multiple nodes in a cluster, maximizing parallel processing capabilities.
 

# What is SPARK? 
* Distributed computing engine that distributes our data to process it. 
* If we have 1GB of data and we want to process it.
  * We could use 1 machine to process it….or...
  * We could use a CLUSTER of machines and scale this to an infinite number, there is NO LIMIT to how much we can scale these clusters in SPARK. 
   * Distributed scaling is the hallmark of why SPARK is favored for BIG DATA workloads. 


# SPARK Architecture
* This is often called the **“Master and Slave”** Architecture. 
* Workflow of SPARK:
   * Driver Program —> Cluster Manager —> Worker Nodes 
* How this works
   * 1. Creates a driver node —> breaks down the information 
   * 2. Sends info to Cluster Manager —> Creates 2 Worker Nodes 
   * 3. Info then send to 2 Worker Nodes to execute data transformations to breakdown the work in to “smaller and smaller tasks”. 
      * Tasks
      * Cache


# Why use SPARK when we have HADOOP?
* 1. In memory computation
   * We can use ALL memory that SPARK has to process BIG DATA. 
* 2. **Lazy Evaluation**
   * Plan is created first —> then executes transformations (hence “lazy”)
* 3. Fault Tolerant
   * Ability to traceback all transformations 
* 4. Partitioning 

# What the heck is Lazy Evaluation?
* Lets say we have 3 data transformations. 
* We would expect that each of the 3 transformations are executed one by one. 
   * However, it will store this in a “logical plan” according to optimizing the compute power. 
* Finally, the “Action” is executed once the **LOGICAL PLAN** has been created. 


# What the heck is a SPARK JOB? 
* At the most simplest level, it is the code that we submit in every cell. 
* Each job is divided into a stage. 
* Each stage can have many smaller tasks. 


# APIs in PYSPARK
* Most of this is common knowledge, but let's list them anyways:
   * 1. Python —> PySpark
   * 2. Scala
   * 3. SQL
   * 4. R




