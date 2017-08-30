# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
def ratate(matrix):
    """
    :type matrix:List(List(Int))
    :rtype:List(List(Int))
    """

    #your code here
    if matrix == [[]]: #m1无法转成数组，所以过滤掉了
        return matrix
    else:    
        arr = np.array(matrix).T  #将列表转化成数组并运用T转置
        a=sorted([i for i in range(len(matrix))],reverse=True) #建立索引
        arr1=arr[:,a]
        return arr1.tolist()    #将数组转化为列表

m1=[[]]
m2=[[1]]
m3=[[i for i in range(3)]for j in range(3)]
m4=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

assert ratate(m1) ==[[]]
assert ratate(m2) ==[[1]]
assert ratate(m3) ==[[0,0,0],[1,1,1],[2,2,2]]
assert ratate(m4) ==[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]