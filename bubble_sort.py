# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 08:31:26 2018

@author: prince khera
"""
t = int(input())
for i in range(t):
    n = int(input())
    a = []
    a = [int(x) for x in input().split()]
    s = False
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                s = True
        if s==False:
            break
    for i in a:
        print(i,end=' ')