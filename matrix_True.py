# -*- coding: utf-8 -*-
def ratate(matrix):
    """
    :type matrix:List(List(Int))
    :rtype:List(List(Int))
    """
    #your code here
    t=len(matrix)-1
    for n in range(len(matrix)//2):
       for i in range((len(matrix)+1)//2):
           matrix[n][i],matrix[t-i][n],matrix[t-n][t-i],matrix[i][t-n]=matrix[t-i][n],matrix[t-n][t-i],matrix[i][t-n],matrix[n][i]
    return matrix
    
    
m1=[[]]
m2=[[1]]
m3=[[i for i in range(3)]for j in range(3)]
m4=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]  

assert ratate(m1) ==[[]]
assert ratate(m2) ==[[1]]
assert ratate(m3) ==[[0,0,0],[1,1,1],[2,2,2]]
assert ratate(m4) ==[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]

