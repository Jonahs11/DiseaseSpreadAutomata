#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:39:34 2020

@author: jonah
"""
import matplotlib.pyplot as plt
import random
import simvars
#
def gens(mat,mat3):

    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if y > 0 and y < simvars.length - 1 and x > 0 and x < simvars.length -1:
                
                
                if mat[y][x] == simvars.uninfec and mat3[y][x] >= (simvars.posplace - 2):
                    
                    count = 0
            
                    if mat[y-1][x] == simvars.infec:
                        count += 1
                    if mat[y][x-1] == simvars.infec:
                        count += 1
                    if mat[y+1][x] == simvars.infec:
                        count += 1
                    if mat[y][x+1] == simvars.infec:
                        count += 1
                    if mat[y-1][x-1] == simvars.infec:
                        count += 1
                    if mat[y+1][x+1] == simvars.infec:
                        count += 1
                    if mat[y+1][x-1] == simvars.infec:
                        count += 1
                    if mat[y-1][x+1] == simvars.infec:
                        count += 1
                        
                        
                    mat3[y][x] = infected(count)
                    
                    
def changing(mat,mat3,mat4):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            
            if mat3[y][x] == 0:
                mat[y][x] = simvars.infec
            
            if mat4[y][x] == 0:
                mat[y][x] = simvars.rest
            
            
                    
                        
                    

def infected(count):
    ran = random.random()
    if count == 0:
        return simvars.posplace
    
    if count  == 1:
        if ran < simvars.ci1:
            val = incub()
            return val
        else:
            return simvars.posplace
        
    if count == 2:
        if ran < simvars.ci2:
            val = incub()
            return val
        else:
            return simvars.posplace
        
    if count == 3:
        if ran < simvars.ci3:
            val = incub()
            return val
        else:
            return simvars.posplace
        
    if count == 4:
        if ran < simvars.ci4:
            val = incub()
            return val
        else:
            return simvars.posplace
        
    if count == 5:
        if ran < simvars.ci5:
            val = incub()
            return val
        else:
            return simvars.posplace
        
    if count == 6:
        if ran < simvars.ci6:
            val = incub()
            return val
        else:
            return simvars.posplace
    
    if count == 7:
        if ran < simvars.ci7:
            val = incub()
            return val
        else:
            return simvars.posplace
    
    if count == 8:
        if ran < simvars.ci8:
            val = incub()
            return val
        else:
            return simvars.posplace
        
def recovery(mat3,mat4,mat):
    for y in range(len(mat3)):
        for x in range(len(mat3[y])):
            
            if mat3[y][x] == 0:
                mat4[y][x] = recoverydesig()
                          
            
    
def recoverydesig():
    rand = random.random()

    if rand < simvars.rr1:
        return simvars.rt1
    
    elif rand >= simvars.rr1 and rand < simvars.rr2:
        return simvars.rt2
    
    elif rand >= simvars.rr2 and rand < simvars.rr3:
        return simvars.rt3
    
    elif rand >= simvars.rr3 and rand < simvars.rr4:
        return simvars.rt4
    
    elif rand >= simvars.rr4 and rand < simvars.rr5:
        return simvars.rt5


                
                
                    
def time(mat3,mat4):
    for y in range(len(mat3)):
        for x in range(len(mat3[y])):
            if y > 0 and y < simvars.length -1 and x > 0 and x < simvars.length -1:
                
                mat3[y][x] += 1
                
                mat4[y][x] += 1
    
        
    
    
def incub():
    rand = random.random()
    
    if rand < simvars.incubr1:
        return simvars.it1
    
    elif rand >= simvars.incubr1 and rand < simvars.incubr2:
        return simvars.it2
    
    elif rand >= simvars.incubr2 and rand < simvars.incubr3:
        return simvars.it3
    
    elif rand >= simvars.incubr3 and rand < simvars.incubr4:
        return simvars.it4
    
    elif rand >= simvars.incubr4 and rand < simvars.incubr5:
        return simvars.it5
        
        
    
def firstgenset(mat,mat3,mat4):
    if simvars.gencount == 0:
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                if y > 0 and y < simvars.length - 1 and x > 0 and x < simvars.length -1:
                    
                    if mat[y][x] == simvars.infec:
                        mat3[y][x] = 0
                            
                        r = random.random()
                        if r < simvars.rr1:
                            mat4[y][x] = simvars.rt1
                        
                        
                        elif r >= simvars.rr1 and r < simvars.rr2:
                            mat4[y][x] = simvars.rt2
                        
                        
                        elif r >= simvars.rr2 and r < simvars.rr3:
                            mat4[y][x] = simvars.rt3
                        
                            
                        elif r >= simvars.rr3 and r < simvars.rr4:
                            mat4[y][x] = simvars.rt4
                        
                            
                        elif r >= simvars.rr4 and r < simvars.rr5:
                            mat4[y][x] = simvars.rt5

    
def prefillcounter(mat,leng):
    for y in range(len(mat)):
            for i in range(simvars.length):
                mat[y].append(simvars.posplace)
                
                
            
            
def borderzeros(lis,length):
    for y in range(len(lis)):
        for x in range(len(lis[y])):
            if y == 0 or y == length-1:
                lis[y][x] = 0
            elif x == 0 or x == length-1:
                lis[y][x] = 0
                
def tablecreate(lis,num):
    for i in range(len(lis)):
        for x in range(num):
            lis[i].append(0)
            ran = random.random()
            if ran < simvars.startinginfec:
                lis[i][x] = 1
                
def stats(mat):
    totalinfec = 0
    totalpop = (simvars.length - 2) ** 2
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            
            if mat[y][x] == simvars.infec or mat[y][x] == simvars.rest:
                totalinfec += 1
            
    avginfec = totalinfec / totalpop
    avginfecpct = (avginfec * 100) // 1
            
    print("After " + str(simvars.gencount) + " generations, " + str(totalinfec) + " people out of a total of " + str(totalpop) + " have been infected.")
    print("That is a total infection rate of over " + str(avginfecpct) + "%.")
    
    
    
def graphs(mat):
    popinfec = 0
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if mat[y][x] == simvars.infec or mat[y][x] == simvars.rest:
                popinfec += 1
    simvars.data[simvars.gencount] = popinfec
        
    if simvars.gencount == (simvars.numgens - 1):
        print(simvars.data)                
        genlis = list()
        numforgen = list()
        for k,v in simvars.data.items():
            genlis.append(k)
            numforgen.append(v)
    
        plt.plot(genlis,numforgen)
        plt.xlabel("# of Generations.")
        plt.ylabel("# of Infections.")
    
    
    
    
    
    
    
    
    
 