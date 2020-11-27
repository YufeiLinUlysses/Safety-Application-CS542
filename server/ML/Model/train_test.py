# written by Jingfeng Xia, jxia@wpi.edu

import LR
import numpy as np
import math

def train(X, Y, alpha=0.01, n_epoch=100):
    # number of features
    p = X.shape[1]
    # number of classes 
    c = int(max(Y))

    # randomly initialize W and b
    W = np.asmatrix(np.random.rand(c,p))
    b= np.asmatrix(np.random.rand(c,1))

    for _ in range(n_epoch):
        # go through each training instance
        for x,y in zip(X,Y):
                y = int(y)-1
                x = x.T # convert to column vector
                # Forward pass: compute the logits, softmax and cross_entropy 
                (z,a,l) = LR.forward(x,y,W,b)
                # Back Propagation: compute local gradients of cross_entropy, softmax and logits
                (dL_da,da_dz,dz_dW,dz_db) = LR.backward(x,y,a)
                # compute the global gradients using chain rule
                dL_dz = LR.compute_dL_dz(dL_da,da_dz)
                dL_dW = LR.compute_dL_dW(dL_dz,dz_dW)
                dL_db = LR.compute_dL_db(dL_dz,dz_db)
                # update the paramters using gradient descent
                W = LR.update_W(W, dL_dW, alpha)
                b = LR.update_b(b, dL_db, alpha)
    return W, b

def predict(Xtest, W, b):
    n = Xtest.shape[0]
    c = W.shape[0]
    Y = np.zeros(n) # initialize as all zeros
    P = np.asmatrix(np.zeros((n,c)))

    for i, x in enumerate(Xtest):
        x = x.T # convert to column vector
#         print(type(x))
        z = np.asmatrix(np.zeros(b.shape))
        z = np.dot(W,x) + b
        a = np.mat(np.zeros(z.shape))
        for j in range(0,z.shape[0]):
            a[j] = np.exp(z[j])
        a /= np.sum(a)
        Y[i] = np.argmax(a)+1
        P[i] = a.T

    return Y, P

def accuracy(test_y_or_train_y,Y):
    true = 0
    rows = Y.shape[0]
    for i in range(0,rows):
        if Y[i] == test_y_or_train_y[i]:
            true+=1
        else:
            pass
    accuracy = true/rows
    return accuracy