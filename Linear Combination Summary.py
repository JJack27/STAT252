#-------------------------------------------------------------------------------
# Name:        Linear Combination Summary
# Purpose:
#
# Author:      yizhou
#
# Created:     23/02/2016
# Copyright:   (c) yizhou 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

def calEstimate(coef, ys):
    a = 0
    for i in range(len(coef)):
        a += coef[i]*ys[i]
    return a

def calMSE(SSE, ns):
    df = sum(ns)-len(ns)
    return SSE/df

def calMST(SSB, ns):
    df = ns[0]-1
    return SSB/df

def calSSB(ys,ns):
    y_bar = sum(ys)/len(ys)
    SSB = 0
    for i in range(len(ys)):
        a = (ys[i]-y_bar)*(ys[i]-y_bar)
        a = a * ns[i]
        SSB += a
    return SSB

def calSSE(ys,std,ns):
    SSE = 0
    for i in range(len(ys)):
        a = std[i]*std[i]*(ns[i]-1)
        SSE += a
    return SSE

def calSE(MSE, coef, ns):
    sqrt_MSE = math.sqrt(MSE)
    a = 0
    for i in range(len(ns)):
        a += (coef[i]**2)/ns[i]
    sqrt_a = math.sqrt(a)
    return sqrt_a*sqrt_MSE

def calCI(estimate, t, SE):
    lower = estimate - t*SE
    higher = estimate + t*SE
    return [lower, higher]

def cal_MSE(ns, std):
    MSE = 0
    for i in range(len(ns)):
        a =(ns[i]-1)*std[i]**2
        MSE += a
    MSE = MSE / (sum(ns)-len(ns))
    return MSE


def main():
    #ys = [25.5999,26.7061, 28.2070, 33.2476, 34.1239, 37.3222]
    #ns = [10,10,10,10,10,10]
    #std = [5.59255,5.13037,4.00454,4.50070,5.80158,4.88503]
    #coef = [-0.5,-0.5,0,0.5,0,0.5]
    #coef = [-1/3,1/3,-1/3,-1/3,1/3,1/3]
    confidence = 0.95
    alpha_test = (1-confidence)/2
    t = 2.048
    ys = [0.6499,0.4092,0.4894,0.4135]
    ns = [8,8,8,8]
    std = [0.0944,0.0664,0.1625,0.1090]
    coef = [1/3,-1,1/3,1/3]
    m = len(ns)*(len(ns))/2
    SSB = calSSB(ys,ns)
    SSE = calSSE(ys,std,ns)
    MST = calMST(SSB,ns)
    #MSE = calMSE(SSE,ns)
    MSE = cal_MSE(ns,std)
    SE = calSE(MSE,coef,ns)
    estimate = calEstimate(coef,ys)
    CI = calCI(estimate,t, SE)
    print('SSB =',SSB)
    print('SSE =',SSE)
    print('MST =',MST)
    print('MSE =',MSE)
    print('-----------------------------')
    print('Estimate =',estimate)
    print('SE =',SE)
    print('-----------------------------')
    print(str(confidence*100),'% Confidence Interval:',sep = '')
    print(CI)

if __name__ == '__main__':
    main()
