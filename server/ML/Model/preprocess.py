# written by Jingfeng Xia, jxia@wpi.edu

import numpy as np
import Get_Data
import scipy
from scipy import stats

def split(data_rows):
    # raw data "innerjoint.csv"
    raw = Get_Data.Get_INNERJOINT_Data()
    # print(raw[0:10])

    # randomly take "data_rows" samples from raw data
    rand = np.arange(np.array(raw).shape[0])
    np.random.shuffle(rand)
    subset = np.array(raw)[rand[0:data_rows]]
    # print(subset.shape)
    # print(subset[0:10])

    # drop column "CRIME_NUMBER","CODE","NAME"
    subset_slice = np.array(subset)[:,3:]
    # print(subset_slice[0:10])

    # turn all strings in array into floats
    data = np.mat(np.zeros(subset_slice.shape))
    data = subset_slice.astype(np.float)
    # print(data[0],type(data[0][4]))

#     # LATITUDE-36, LONGTITUDE+78, to ,make both distributes around 6
#     data[:,3] -= 36
#     data[:,4] += 78

    # if "SHOOTING" = "T", turn "DANGER" to 3
    for i in range(0,data.shape[0]):
        data[i,-2] = max(data[i,-2],data[i,-1])
    data = data[:,0:-1] # drop the potential lower one
    # print(data[0:10])
    
    # z_score
    data = np.array(data.T)
    for i in range(0,data.shape[0]-1):
#         print(np.mean(data[i]),np.std(data[i]))
        data[i] = stats.zscore(data[i])
    data = data.T
    
    X = data[:,0:-1] # features: MONTH,DAY_OF_WEEK,HOUR,LATITUDE,LONGTITUDE
    Y = data[:,-1] # label(DANGER)
    # print(X.shape, X.dtype)
    # print(Y.shape, Y.dtype)
    
    return X, Y