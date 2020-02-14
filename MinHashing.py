# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:05:54 2018

@author: Apostolhs Salwmidhs 2351
"""

from numpy import loadtxt
import numpy as np
import random

def MinHashing(namefile,n):
    A  = loadtxt(namefile)#pinakas mitroou ths morfhs KxN
    K = len(A)#grammes
    N = len(A[0])#sthles
    S = np.ones((n, N))#upografes pinakas mitroou ths morfhs nxN
    S = -S
    for i in range(n):
        a = random.randrange(1, 22)
        b = random.randrange(1, 22)
        f = np.zeros(K)
        k = 0
        while( k < N ):
            f = np.zeros(K)
            for j in range(K):
                f[j] = ((a * j + b) % 23)
            j = 0
            check = True
            minf = min(f)
            print(minf)
            while(minf < 24 and j < K and check):
                if(f[j] == minf):
                   if( A[j][k] == 1.0):
                       S[i][k] = j
                       check = False
                   else:
                        f[j] = 24
                        
                        j = -1
                        minf = min(f)
                j = j + 1
            k = k+1
            
                    
    print("S :")
    print(S)
    print(" ")
    JA = 0
    JS = 0
    sumJA = 0
    for j in range(N - 1):
        l = 1
        while(j + l < N):
            for i in range(K):#Jaccard Similarity A
                if(A[i][j] == A[i][j + l]):
                    if(A[i][j] == 1):
                        JA = JA + 1
                        sumJA = sumJA + 1
                else:
                    sumJA = sumJA + 1
            for i in range(n):#Jaccard Similarity S
                if(S[i][j] == S[i][j + l]):
                    if(S[i][j] != -1.0):
                        JS = JS + 1
            JA = JA / sumJA
            print("Jaccard Similarity A : sim({},{}) = {}".format(j, j + l, JA))
            sumJA = 0
            JA = 0
            JS = JS / n
            print("Jaccard Similarity S : sim({},{}) = {}".format(j, j + l, JS))
            print(" ")
            JS = 0
            l = l + 1
    
    
MinHashing("file.txt",10) 
