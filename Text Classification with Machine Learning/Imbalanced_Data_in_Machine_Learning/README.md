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
* **Resampling is always a good starting point when dealing with imbalanced data. However, it runs the risk of OVERFITTING the training data (over-sampling) and losing important information from removing data (under-sampling).**
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
1. BorderlineSMOTE
   * Based on the ML classifier borderline. 
2. K-Means SMOTE
3. SVM SMOTE
4. SMOTE-NC
   * Used for categorical data (its important to remember that SMOTE itself only works with continuous data).

5. SMOTE-Tomek
   * Uses a combination of SMOTE oversampling and Tomek links undersampling tecniques.

6. SMOTE-ENN
   * Also known as "SMOTE Edited Nearest Neighbors".
   * Very similar to SMOTE-Tomek in that it combines oversampling with undersampling.
     * SMOTE does the oversampling and ENN does the undersampling.
   * ENN is a great way to remove is an excellent method to remove majority class samples in both original and sample result datasets where the nearest class minority misclassifies it.
     * It will remove the majority class close to the border where it was misclassified.

7. SMOTE-CUT
   * Also known as "SMOTE-Clustered Undersampling".
   * This technique combines oversampling, clustering, and undersampling.

8. ADASYN
   * Also known as "Adaptive Synthetic Sampling".
   * This technique oversamples the minority data class based on the density of the dataset.
   * ADASYN will assign a weighted distribution to each of the minority samples and prioritizes oversampoling the minority samples that are harder for the ML model to classify.
  
* References for this section
    * [Handling Imbalanced Data by Oversampling with SMOTE and its Variants](https://medium.com/analytics-vidhya/handling-imbalanced-data-by-oversampling-with-smote-and-its-variants-23a4bf188eaf)
    * [Undersampling and oversampling: An old and a new approach](https://medium.com/analytics-vidhya/undersampling-and-oversampling-an-old-and-a-new-approach-4f984a0e8392)
    * [7 SMOTE Variations for Oversampling](https://www.kdnuggets.com/2023/01/7-smote-variations-oversampling.html)


### Under-Sampling or Downsampling - Remove examples from majority class
1. **Random under-sampling**
   * Randomly removes samples from the majority class until a specific ratio is reached.
   * Important point to remember: Random under-sampling may result in the final dataset being too small for a model to actually learn from the data. This may only work well when there is enough samples (e.g. at least 1000 samples) in the minority class.
  
 ![image](https://github.com/user-attachments/assets/3964e671-cd9b-4e99-8558-5af5f4dae9dc)

  
2. **Tomek Links**
   * Tomek Links is an under-sampling technique that was developed in 1976 by Ivan Tomek.
   * It is a modification of the **Condensed Nearest Neighbors (CNN)**.
   * It can be used to find desired samples of data from the majority class that is having the lowest Euclidean distance with the minority class data and then remove it.
   * Main Advantage of this method: It may help make the decision boundary more clear so the model can more easily learn the classification boundary.
       * However, the model may still not be able to learn the true nuances of the decision boundary for classification. 
  
![image](https://github.com/user-attachments/assets/94e2eaa0-303e-4f86-af44-628658e0994c)





 ## Machine Learning Model Methods for Imbalanced Data
 * Basic concept with this approach is to make the ML model(s) more robust to class imbalance.
 * This will NOT change the distribution of the training data.

 1. **Update Loss Function of the ML model -- Cost Sensitive Learning**
    * You can design a loss function that will penalize the wrong classification of the minority class more than the wrong classification of the majority class.
    * This will ultimately force the ML model to treat specific classes with more weight than the others during model training.
    * This focuses on modifying learning algorithms optimization functions so they minimize the overall cost of misclassification instead of the overall error rate.
        * By assigning specific costs to different types of misclassifications, cost-sensitive learning methods allow ML models to **prioritize the minority class** and achieve better performance in critical classification problems.
    * As an example: **Class-balanced loss**
        * This will make the weight of each class inversely proportinal to the number of samples in that class. 

    * What are the different types of cost? -- these come from the confusion matrix in ML evaluation
      1. false positive (cost of misclassifying the positive class as negative),
      2. false negative (cost of misclassifying the negative class as positive),
      3. true positive (correctly classifying the positive class), and
      4. true negative (correctly classifying the negative class).

* Excellent blog post on Cost sensitive learning: https://www.blog.trainindata.com/cost-sensitive-learning-for-imbalanced-data/

2. **Select Specific Algorithms**
   * Tree-based models will work very well on tasks that involve small and imbalanced datasets.
   * Logistic Regresion is able to handle imbalance by itself pretty well.
       * It does this by adjusting the probability threshold to improve the overall accuracy for predicting the minority class.

3. **Combine Multiple Techniques**
   a. **Under-sampling with Ensemble modeling**
       * This will use all samples from the minority class and a subset of the majority class to train multiple models and then ensemble those models.
   b. **Under-sampling + update loss function**
       * Undersampling the majority class until a certain ratio is reached -->
       * Calculate new weights for both classes -->
       * Pass new weights to loss function of the model



## Evaluation Metrics --- Which ones are best for handling imbalanced datasets?
* You need to remember to choose the appropriate evaluation metric(s) for the task you are performing.
* **IMPORTANT**: use **unsampled data** instead of resampled data to evaluate a model because using resampled data will only cause the model to OVERFIT the resampled data distribution.
    * The test dataset should provide an accurate representation of the original dataset.
 
* **Accuracy** is often **misleading** when classes are imbalanced!
    * Why? Majority class accuracy performance will automatically dominate the metrics not giving you any insight into the actual accuracy of the minority classes.
    * Consider using **accuracy of each individual class instead**. This will be more precise and interpretable.
 
* **Precision, Recall, F1 Score**
    * As we know these metrics measure an ML model's performance with respect to a positive class in a binary or multiclass classification problem.

* **Precision-Recall Curve**
    * This will identify a threshold that works well for yo9ur dataset.
    * It will give more importance to the **positive class** which is very helpful when dealing with imbalanced data.
 

* **AUC of the ROC Curve**
    * Area under the curve of the receiver operating curve.
    * This tunes thresholds to increase Recall and decrease False Positive rates.
    * This will treat BOTH classes equally and is overall less sensitive to model improvements on MINORITY class so its less helpful comopared to **Precision-Recall** curve. 
