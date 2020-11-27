# written by Jingfeng Xia, jxia@wpi.edu
import numpy as np
import math

################# forward ####################

def compute_z(x,W,b):
    # Compute the linear logit value
    W = np.mat(W)
    x = np.mat(x)
    b = np.mat(b)
    z = np.dot(W,x) + b
    return z

def compute_a(z):
    # Compute the softmax activations.
    a = np.mat(np.zeros(z.shape))
    for i in range(0,z.shape[0]):
        if z[i] < -20:
            a[i] = 0.0
        elif z[i] > 20:
            a[i] = 500000000.0
        else:
            a[i] = float(np.exp(z[i]))
    if sum(a) == 0:
        a = np.mat(np.ones(z.shape))/z.shape[0]
    else:
        a /= np.sum(a)
    return a

def compute_L(a,y):
    # Compute multi-class cross entropy
    if a[y] == 0:
        L = 1e5 + 1
    else:
        L = float(-np.log(a[y]))
    return L

def forward(x,y,W,b):
    # compute forward pass z,a,l
    z = compute_z(x,W,b)
    a = compute_a(z)
    L = compute_L(a,y)
    return z, a, L

################ backward ###################

def compute_dL_da(a, y):
    # Compute local gradient of 
    # the multi-class cross-entropy loss function on activations
    dL_da = np.mat(np.zeros(a.shape))
    if a[y] == 0:
        dL_da[y] = float(-1e5 - 1)
    else:
        dL_da[y] = float(-1/a[y])
    return dL_da

def compute_da_dz(a):
    # Compute local gradient of the softmax activations on logits
    c = a.shape[0]
    da_dz = np.mat(np.zeros(shape=(c,c)))
    for i in range(0,c):
        for j in range(0,c):
            if i == j:
                da_dz[i,j] = a[i]*(1-a[i])
            else:
                da_dz[i,j] = -a[i]*a[j]
    return da_dz

def compute_dz_dW(x,c):
    # Compute local gradient of the logits function z w.r.t. the weights W.
    p = x.shape[0]
    dz_dW = np.mat(np.zeros(shape=(c,p)))
    for i in range(0,c):
        dz_dW[i] = x.T
    return dz_dW

def compute_dz_db(c):
    # Compute local gradient of the logits function z w.r.t. the biases b. 
    dz_db = np.mat(np.ones(c)).T
    return dz_db

def backward(x,y,a):
    # Back Propagation: given an instance in the training data, compute the local gradients of the logits z, activations a, weights W and biases b on the instance. 
    dL_da = compute_dL_da(a, y)
    da_dz = compute_da_dz(a)
    c = a.shape[0]
    dz_dW = compute_dz_dW(x,c)
    dz_db = compute_dz_db(c)
    return dL_da, da_dz, dz_dW, dz_db

def compute_dL_dz(dL_da,da_dz):
    # chain rule
    dL_dz = da_dz.dot(dL_da)
    return dL_dz

def compute_dL_dW(dL_dz,dz_dW):
    # chain rule
    dL_dz = np.mat(dL_dz)
    dz_dW = np.mat(dz_dW)
    p = dz_dW.shape[1]
    dL_dW = np.mat(np.zeros(dz_dW.shape))
    for i in range(0,p):
        dL_dW[:,i] = np.multiply(dL_dz,dz_dW[:,i])
    return dL_dW

def compute_dL_db(dL_dz,dz_db):
    # chain rule
    dL_db = np.multiply(dL_dz,dz_db)
    return dL_db 

def update_W(W, dL_dW, alpha=0.001):
    W -= alpha*dL_dW
    return W

def update_b(b, dL_db, alpha=0.001):
    b -= alpha*dL_db
    return b 





