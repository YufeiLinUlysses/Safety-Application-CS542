Blueprint of the safety index predictor

--- by Jeff Xia

1. Kaggle data should be cleansed.
2. PCA to get different vital attributes.
(3, optional). feature engineering then select with best subset, forward stepwise or backword stepwise.
3. 
plan a. Kaggle data is labeled with unsafe 0 and safe 1 with multivariable logistic regression, extend the data to range(0, 100).
plan b. Kaggle data is labeled from 0 to 10 as 11 ranks with softmax logistic regression.
plan c. Neural Networks on Kaggle data is labeled from 0 to 10 as 11 ranks with softmax logistic regression.