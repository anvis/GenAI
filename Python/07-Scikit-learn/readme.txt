Scikit used to Implement ML Models

Sklearn is used for 
Fit and predit estimators,
transformers and pre-processing,
pipelines, 
model evaluations,
Automated parameter search.


Scikit-learn provides dozens of built-in machine learning algorithms and models, called estimators. 
Each estimator can be fitted to some data using its fit method.
Enables .fit() and .predict() method
Both supervised ( Classification and Regression ) and unsupervised

pre-processing step to transform and / or impute the data
In scikit-learn, pre-processors and transformers follow the same API as the estimator objects 
(they actually all inherit from the same BaseEstimator class). 
The transformer objects don’t have a predict method but rather a transform method that outputs a newly 
transformed sample matrix X:
In Estimators we have fit and transform In Preprocessers we have fit and transform.


Transformers and estimators (predictors) can be combined together into a single unifying object: a Pipeline.
 The pipeline offers the same API as a regular estimator: it can be fitted and used for prediction with fit and predict.
  As we will see later, using a pipeline will also prevent you from data leakage, i.e. disclosing some testing data in your training data.




https://www.youtube.com/watch?v=t3ecaDij_pU

https://github.com/anaspmachinelearning/YouTubeTutorials/blob/main/SciKit%20Learn%20Tutorial.ipynb

