# Imbalanced Data in Machine Learning
* A repo devoted to the conundrum that is imbalanced data and various approaches to handling this common problem.


# Background
* Imbalanced datasets are classified as such when 1 or more labels makes up the MAJORITY of the dataset, where 1 or more labeled classes dominates the target prediction class or classes.
* This applies to **classification** and **regression** tasks.

1. **Classification**
   * binary classification
   * multiclass classification
   * multilabel classification
   * multioutput classification
  
2. **Regression**
   * This will usually show up as outlier values that are either MUCH LOWER or HIGHER than the median or average of the dataset distribution.
   * As an example: Predicting housing prices. Houses that are > `$10 million` dollars are rare.
  

# Difficult Scenarios
* Getting more real world data to represent the minority class or classes may be impossible or difficult to acquire because the data is naturally going to be **imbalanced**.
* As an example:
  1. **Fraud Detection**
  2. **Rare Disease**



# What are the disadvantages of imbalanced datasets? Why does it cause so many problems in Machine Learning?
1. ML models are not able to predict the MINORITY class or classes on unseen data (e.g. test set, real world cases).
2. The model is ONLY able to learn simple heuristics (the MAJORITY/DOMINANT class or classes) and immediately gets stuck in suboptimal prediction loops.
3. An ML model training accuracy of `>90%` is often misleading because an ML model may not have the actual predictive power on a rare or MINORITY class.
4. More often than not, the MINORITY class is actually MORE IMPORTANT than the majority class.
   * The wrong prediction of the minority target class can be costly.
   * As an example: **If you misclassify fradulent transactions this can be 100x more costly than misclassifying a well known or common fraud classification.**


# How do we handle imbalanced data? 
* There are 3 levels we can do this at:

1. Data-level: Resampling
2. Machine Learning Model Level
3. Metrics-level

## Resampling (Data Level)
* This will change the training data distribution to significantly reduce the levels of class imbalance.
* Techniques include:

### Over-Sampling or Upsampling --> Add more samples to the minority class.
    a. **Random Over-sampling**
        * Randomly make copies of the minority class until a specific ratio is reached.
        * PROBLEM with this approach: May lead to OVERFITTING of the ML model. 
![image](https://github.com/user-attachments/assets/8a6beafd-dd68-42ac-916d-47df0b6ac346)

    b. **Generate Synthetic Samples**
        * **SMOTE - synthetic minority oversampling technique)**
            * Advantages: Can prevent OVERFITTING by random oversampling because it will not use original samples.
            * Very common approach. Creates synthetic samples of the minority or rare class by combining original samples.
            * It does this using a nearest neighbor approach -- source: [Bordia, 2022](https://medium.com/analytics-vidhya/handling-imbalanced-data-by-oversampling-with-smote-and-its-variants-23a4bf188eaf)
                  * Select a sample, let’s call it O (for Origin), from the minority class randomly
                  * Find the K-Nearest Neighbours of O that belong to the same class
                  * Connect O to each of these neighbours using a straight line
                  * Select a scaling factor ‘z’ in the range `[0,1]` randomly
                  * For each new connection, place a new point on the line (z*100)% away from O. These will be our synthetic samples.
                  * Repeat this process until you get the desired number of synthetic samples


![image](https://github.com/user-attachments/assets/b35ced6a-c188-45b6-bfeb-b46dc5a32f8b)


#### Additional Over Sampling Techniques
* There are other over sampling techniques, check them out:



### 