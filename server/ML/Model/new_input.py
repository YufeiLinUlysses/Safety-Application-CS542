# written by Jingfeng Xia, jxia@wpi.edu

import train_test as TT
import numpy as np

DAY_OF_WEEK = {"MONDAY":1,"TUESDAY":2,"WEDNESDAY":3,"THURSDAY":4,"FRIDAY":5,"SATURDAY":6,"SUNDAY":7}
DISTRICT = {"A1":1,"A15":2,"A7":3,"B2":4,"B3":5,"C11":6,"C6":7,"D14":8,"D4":9,"E13":10,"E18":11,"E5":12}
W = np.mat([[ 0.50925096,0.13611806,0.78839678,0.59964475,1.3605857,0.23798743],
 [ 0.72555654,1.2421177, 0.98460094, 1.34876575,-1.14678045, 0.69558499],
 [ 0.06799253,-0.09379573,0.13527373,0.21858613,2.23813193,-0.20509305]])
b = np.mat([[0.20636326],
 [0.07791212],
 [0.64255383]])

# X feature: MONTH, DAY_OF_WEEK, HOUR,DISTRICT(1:12), LATITUDE-36, LONGTITUDE+78
input = np.array(["9","WEDNESDAY","8","A15","42.2330858","-71.12815697"])

input[1] = DAY_OF_WEEK[input[1]]
input[3] = DISTRICT[input[3]]
input = np.mat(input.astype(np.float))
input[:,4]-=36
input[:,5]+=78

Y,P = TT.predict(input, W, b)
print(Y) # [1.]