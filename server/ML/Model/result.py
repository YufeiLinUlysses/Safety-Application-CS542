# written by Jingfeng Xia, jxia@wpi.edu

import preprocess
import LR
import train_test as TT
import sklearn.model_selection as ms
import numpy as np
import math

# get 5000 rows of cleansed data
# X feature: MONTH,DAY_OF_WEEK,HOUR,DISTRICT(1:12),LATITUDE-36,LONGTITUDE+78
# Y label: DANGER(1,2,3)->low,medium, high
(X,Y)= preprocess.split(20000)

# get training set and test set
train_x, test_x, train_y, test_y = \
    ms.train_test_split(X, Y, test_size=0.2, random_state=7) # training:test = 8:2
# print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

# alpha, n_epoch can be tuned
W,b = TT.train(np.mat(train_x), train_y, alpha=0.03, n_epoch=50)
# get W,b for further use
print("W:",W)
print("b:",b)
Y_tr,P_tr = TT.predict(np.mat(train_x), W, b)
Y_te,P_te = TT.predict(np.mat(test_x), W, b)

test_acc = TT.accuracy(test_y,Y)
train_acc = TT.accuracy(train_y,Y)

train_acc = TT.accuracy(train_y,Y_tr)
print("train accuracy:",train_acc)
test_acc = TT.accuracy(train_y,Y_te)
print("test accuracy:",test_acc)