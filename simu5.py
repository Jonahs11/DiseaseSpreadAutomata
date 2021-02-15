#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:03:14 2020

@author: jonah
"""
import simfuncs
import simvars
def main():
    mat1 = [[] for i in range(simvars.length)]
    mat2 = [[] for i in range(simvars.length)]
    mat3 = [[] for i in range(simvars.length)]
    mat4 = [[] for i in range(simvars.length)] #used for variation of recovery time
    
    
    simfuncs.tablecreate(mat1,simvars.length)
    simfuncs.borderzeros(mat1,simvars.length)
    simfuncs.prefillcounter(mat3,simvars.length)
    simfuncs.prefillcounter(mat4,simvars.length)
    
    simfuncs.firstgenset(mat1,mat3,mat4)
    
    
    
    flag = True
    
    while simvars.gencount < simvars.numgens:
        if flag == True:
            simfuncs.time(mat3,mat4)
            simfuncs.changing(mat1,mat3,mat4)
            simfuncs.gens(mat1,mat3)
            simfuncs.recovery(mat3,mat4,mat1)
            simfuncs.stats(mat1)
            mat2 = mat1
            
            for y in range(len(mat2)):
                print(mat2[y]),
            
            print(" ")
            simfuncs.graphs(mat2)
        
            flag = False
        
        else:
            simfuncs.time(mat3,mat4)
            simfuncs.changing(mat1,mat3,mat4)
            simfuncs.gens(mat2,mat3)
            simfuncs.recovery(mat3,mat4,mat2)
            simfuncs.stats(mat2)
            mat1 = mat2
            
            for y in range(len(mat1)):
                print(mat1[y]),
                
            print(" ")
            simfuncs.graphs(mat1)
        
            flag = True
        simvars.gencount += 1
        '''
        for y in range(len(mat2)):
            print(mat3[y]),
        print(" ")
                    
        for y in range(len(mat2)):
            print(mat4[y]),
        print(" ")
        '''
                    
                                 
            
            
    
                
main()
    