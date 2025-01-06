# Machine Learning in PySpark
* Machine Learning using MLlib in PySpark. 


# MLlib
* Scikit learn does not distribute over a spark df. 
* Therefore, MLlib offers machine learning packages of its own to use with Apache Spark/PySpark API
* Full Spark MLlib docs: https://spark.apache.org/docs/latest/ml-guide.html

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
