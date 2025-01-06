# Machine Learning in PySpark
* Machine Learning using MLlib in PySpark. 


# MLlib
* Scikit learn does not distribute over a spark df. 
* Therefore, MLlib offers machine learning packages of its own to use with Apache Spark/PySpark API
* Full Spark MLlib docs: https://spark.apache.org/docs/latest/ml-guide.html
* Spark ML API docs: https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html

## Clustering Algorithms
1. K-means
2. LDA
3. Bisecting k-means
4. Gaussian Mixture Model (GMM)

## Collaborative Filtering 
* PySpark uses the ALS or Alternating Least Squares Algorithm: https://spark.apache.org/docs/latest/ml-collaborative-filtering.html

## Frequent Pattern Mining Algorithms
1. FP-Growth
2. PrefixSpan

## Classification Algorithms
1. Logistic Regression
2. Binomial logistic regression
3. Multinomial logistic regression
4. Decision tree classifier 
5. Random forest classifier
6. Gradient-boosted tree classifier
7. Multilayer perceptron classifier (MLP -- neural networks)
8. Linear SVM
9. One-vs-Rest classifier 
10. Naive Bayes


## Regression 
1. Linear Regression 
2. Generalized Linear Regression 
3. Decision Tree regression
4. Random Forest regression 
5. Gradient-boosted tree regression 
6. Survival Regression 
7. Isotonic Regression


## Other MLlib Machine Learning Features
* Hyperparameter tuning (e.g. model selection)
* Cross-validation
* Vectorizor Assembler
* Train-Validation Splits 
* Pipelines
* Basic Stats
      * Correlation
      * Hypothesis Testing
* Optimization of linear methods (developer)
      * Limited-memory BFGS (L-BFGS)
      * Normal equation solver for weighted least squares
      * Iteratively reweighted least squares (IRLS)




# MLlib Data Format Requirements 
1. ML features (e.g. independent variables) should always be in a DENSE VECTOR FORMAT.
2. Spark expects ALL FEATURES TO BE NUMERICAL. 
3. Classfication algorithms
  * Spark always starts indexing at 0 label
4. PySpark has functions to handle ALL OF THE ABOVE!


## Spark Required Data Formats
1. All features (independent variables) need to be NUMERIC and DENSE VECTOR formats.
     * This means you need to transform data before you can utilize it in any ML algorithms. 
     * Spark also assumes that you have done the following:
          * Dependent Variable (Target) is in a column called “label”.
          * Independent Variables (features) are in a column called “features”.
2. Classification Algorithms
     * Spark expects a “0” indexed label (similar to Python indexing).
     * For Naive Bayes classifier, Spark expects all features to be NON-NEGATIVE. —> there is no built in function for this. 



# Spark Machine Learning — Model Selection & Hyperparameter Tuning Workflow
1. Load and pre-process dataset(s).
2. Hyperparameter optimization using cross-validation 
3. Fitting tuned algorithm to training data. 
4. Apply fitted/trained model to test dataset.


## Cross Validation
* Spark has a built-in function called `CrossValidator`
* docs: https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.tuning.CrossValidator.html
* How this works:
     * Splits into k-folds for Train and Test datasets. 
     * As example: k = 5 folds —> 4/5 for train and 1/5 for testing. 
* Final fitting on best k fold parameters.


## Skewness

### Diagnosing Data Skewness
* If 0 —> data is symmetric
* Positive skewness —> greater num of small values
* Negative skewness —> greater num of large values
* As a “rule of thumb”
     * if skewness is less than -1 or greater than 1, distribution is HIGHLY skewed
     * if skewness is between -1 and -0.5 or between 0.5 and 1, distribution is moderately skewed. 
     * if skewness is between -0.5 and 0.5, distribution is approximately symmetric. 

### Handling Data Skewness
* The goal is to create a normal distirbution 
* To treat skewed data, you would either:
     * Log transformation for positive skewed data
     *....Or...
     * Exponential transformation for negatively skewed data.
 

## Outliers in Spark
* Spark doesn’t have built in methods for dealing with outliers.
* This is also known as “Flooring” and “Capping”. 
* Usually this means editing any value that is above or below a statistica threshold (e.g. 99th percentile or 1st percentile) back to highest or lowest value in that percentile. 
* As an example:
     * If the 99th percentile is 96 and there is a value of 1,000, that value is changed to 96.
 


# Feature Selection 
* We all know how common feature selection is in Machine Learning. 

1. For Decision Trees including Random Forests and Gradient Boosted Trees
   * we can perform this process using —> “Feature Importance Score Estimate” of the importance of each feature. 
   * The importance of each feature is the average of its importance across all trees.
   * As an example: 
     * If we have 2 variables:
     * Score of 1 variable is .75, the other would be .25 —> which adds up to 1.
    

2. For linear regression, Logistic Regression and LinearSVM.
   * If the coefficients can be used to understand variable significance relative to one another. 
     * Ideally we want NO CORRELATION for our models to perform well.


# Machine Learning Pipelines in Spark
* Spark Trains multiple transformers and estimators together. 
* This Streamlines machine learning. 
* Each stage is either a transformer or an estimator. 
* The 2 basic pipelines are as follows -- (source)[https://spark.apache.org/docs/latest/ml-pipeline.html]

1. Pipeline (estimator) using transformers:

* Tokenizer —> HashingTF —> Logistic Regression

2. Pipeline.fit()
Raw Text —> Words —> Feature vectors —> Logistic Regression Model 


![image](https://github.com/user-attachments/assets/628c85e6-a0fc-42b8-8f24-c718e5c82ddc)



## A Pipeline is an Estimator
* Thus, after a Pipeline’s fit() method runs, it produces a PipelineModel, which is a Transformer.
* This PipelineModel is used at test time; the figure below illustrates this usage. (source)[https://spark.apache.org/docs/latest/ml-pipeline.html]


![image](https://github.com/user-attachments/assets/f8e0dbee-6e0b-45df-bad6-56ab8cad245a)





