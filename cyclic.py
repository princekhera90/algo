# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:33:35 2018

@author: prince khera
"""

class graph(): # class to make a graph
    def __init__(self,nn):
        self.nn = nn # nn=no. of nodes
        self.d = {}
        
    def add_edge(self,sn,en):# sn = start node and en = end node
        self.d[sn] = self.d.get(sn,[])
        self.d[sn].append(en)
        
    def is_cyclic(self):
        visited = {}# if a particular node is visited once
        for i in self.d.keys():
            visited[i] = False
        for key in self.d:
            if key in self.d[key]:#for self cycle
                return key,key
            for i in self.d.keys():
                if self.d.get(i,0) != 0:#if some node is not in list
                    if key in self.d[i] and visited[key]==False:
                        return key,i
        return False
                        
                
        
g = graph(4)
g.add_edge(0,1)
g.add_edge(3,0)
g.add_edge(1,2)
g.add_edge(1,0)    
g.add_edge(2,0)
g.add_edge(0,3)  
r = g.is_cyclic()
if r == False:
    print('there is no cycle')
else:
    print(str(r[0])+'-->'+str(r[1]))