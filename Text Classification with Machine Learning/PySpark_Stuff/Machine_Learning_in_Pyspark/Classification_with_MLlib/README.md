# Classification Algorithms using MLlib in PySpark


## Dependent Variable Pre-processing for Classification
1. PySpark has a built-in function for this called `String Indexer`
* This function is very handy when your Categorical or label column is a text value. 
  * PySpark requires the “label” column to be stored as a numeric value and this function automatically converts labels to numbers. 
* The function `IndexToString` converts string labels back to indexes. 


2. `OneHotEncoderEstimator`
* Another function to transform the dependent variable. 
* This is similar to the sklearn method in Python. 


## Classification Algorithms supported in PySpark
1. Binary Classification
2. Multinomial Classification

## Specific Algorithms
1. Logistic Regression -- estimates probability of event occuring given data --> outputs logits between 0 and 1.
2. Decision Trees
   * Build classificaiton or regression models as trees. 
   * Decision nodes and leaf nodes. 
   * Suffer from overfitting and high variance --> Prone to “noise” in 1 tree. 

3. Ensemble Learning
  * This is a better solution to Decision Trees.
  * Essentially a Collection of predictors 
  * Examples: Random Forest & Gradient Boosting 

      * Random Forest (Bagging)
          * handles overfitting 
          * reduces variance and “noise” with multiple trees. 
          * independent classifiers 
          * Trains models independently in parallel on different subsets of the data. The predictions from each model are then combined, usually by averaging or voting, to produce the final prediction. Bagging is often used with unstable models like decision trees.

      * Gradient Boosting (Boosting)
          * Hierarchical approach 
          * objective is to reduce loss function 
          * Can overfit significantly
          * Reduces bias and variance 
          * Sequential classifiers
       

4. Multilayer Perceptron Classifier
* Feedforward ANN
* 3 layers
      * Input —> # features
      * hidden layer —> input layer + 1
      * output layer —> # classes predicting



5. Linear SVM
  * Vectors further from hyperplane —> more confident in classification predictions 

6. One-vs-rest classifier
  * Single classifier trained per class 
  * Can have multiple issues 

7. Naive Bayes
  * Based on bayes theorem 


