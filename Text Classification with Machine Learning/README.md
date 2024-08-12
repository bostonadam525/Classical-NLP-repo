# Text Classification with Machine Learning
* This repo contains Text Classification projects and experiments using "classical" supervised machine learing algorithms (not deep learning or transformers).
* Some of the most common text classification machine learning algorithms used in this repo:
1. Logistic regression
2. Naive Bayes
3. SVM
4. KNN
5. XGBoost
6. Random Forest


# Comparison of Multi classification methods

* **Binary classification**
  * Only 2 classes to predict, each instance belongs to either of them. e.g. Classifying an image of an animal into cat or dog category.
* **Multiclass classification**
  * Each data point belongs to 1 class
* **Multi-label classification**
  * Data points can be associated with **multiple classes** at the same time.

## Machine Learning Metrics, etc..
* An output layer of a multiclass classification model will usually consist of only 1 node per class.
* However, the output layer of a multi-label classification, will have each class represented by 1 node, and multiple nodes can be active at the same time.
* Machine Learning evaluation metrics are different for both techniques.
    * 1. **Accuracy** is mostly used for **multiclass classification.**
    * 2. ****Precision, recall, and the F1-score** are better suited for **multi-label classification.**
