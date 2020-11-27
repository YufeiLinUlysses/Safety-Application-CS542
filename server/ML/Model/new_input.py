# written by Jingfeng Xia, jxia@wpi.edu

import train_test as TT
import numpy as np


DAY_OF_WEEK = {"MONDAY":1,"TUESDAY":2,"WEDNESDAY":3,"THURSDAY":4,"FRIDAY":5,"SATURDAY":6,"SUNDAY":7}
# DISTRICT = {"A1":1,"A15":2,"A7":3,"B2":4,"B3":5,"C11":6,"C6":7,"D14":8,"D4":9,"E13":10,"E18":11,"E5":12}
# data_num = 20000
# alpha = 0.02
# n_epoch = 50
# train accuracy: 0.467625
# test accuracy: 0.474

W = np.mat([[0.70589358, 0.57894807, 0.57555195, 0.64646587, 0.45634837],
 [0.69749017, 0.56445017, 0.38924738, 0.67382041, 0.68272357],
 [0.67179093, 0.5696221, 0.65087029, 0.95102331, 0.32250566]])
b = np.mat([[0.4704748],
 [0.83051006],
 [-0.48455419]])

# X feature: MONTH, DAY_OF_WEEK, HOUR, LATITUDE-36, LONGTITUDE+78
raw_input = np.array([["4","SATURDAY","23","42.30540715","-71.06547135"],
                 ["9","SUNDAY","19","42.30021944","-71.06311002"],
                 ["2","WEDNESDAY","12","42.34044966","-71.08845935"],
                 ["5","THURSDAY","20","42.2330858","-71.12815697"],
                 ["6","SUNDAY","2","42.34455947","-71.14890849"],
                 ["1","WEDNESDAY","8","42.35241815","-71.06525499"],
                 ["3","FRIDAY","3","42.32866284","-71.08563401"],
                 ["10","WEDNESDAY","0","42.32866284","-71.08563401"],
                ["7","FRIDAY","22","42.23649723","-71.12935123"]])
for i in range(0,raw_input.shape[0]):    
    raw_input[i,1] = DAY_OF_WEEK[raw_input[i,1]]
#     raw_input[i,3] = DISTRICT[raw_input[i,3]]
input = np.mat(raw_input.astype(np.float))

# z_score with mean, std from big data
input = input.T
mean = [6.581255,3.9459,13.29537,42.322349287354555,-71.0826005364158]
std = [3.275075209056275,1.9669222633342682,6.271098513267034,0.03175847257436829,0.02939035430914813]
for i in range(0,input.shape[0]):
    input[i] = (input[i]-mean[i])/std[i]
input = input.T
# print(input)

Y,P = TT.predict(input, W, b)
print(raw_input)
print(Y)