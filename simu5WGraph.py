#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:03:14 2020

@author: jonah
"""
import simfuncs
import simvars
import matplotlib.pyplot as plt

data = dict()


def main():
    # 4 matricies, two used for storing states of individuals, one for incubation time tracked
    # and one for recovery time tracker
    mat1 = [[] for i in range(simvars.length)]
    mat2 = [[] for i in range(simvars.length)]
    mat3 = [[] for i in range(simvars.length)]
    mat4 = [[] for i in range(simvars.length)]  # used for variation of recovery time

    simfuncs.tablecreate(mat1, simvars.length)
    simfuncs.borderzeros(mat1, simvars.length)
    simfuncs.prefillcounter(mat3)
    simfuncs.prefillcounter(mat4)

    simfuncs.firstgenset(mat1, mat3, mat4)

    flag = True

    while simvars.gencount < simvars.numgens:
        if flag == True:
            simfuncs.time(mat3, mat4)
            simfuncs.changing(mat1, mat3, mat4)
            simfuncs.gens(mat1, mat3)
            simfuncs.recovery(mat3, mat4, mat1)
            simfuncs.stats(mat1)
            mat2 = mat1

            for y in range(len(mat2)):
                print(mat2[y]),

            print(" ")

            flag = False

        else:
            simfuncs.time(mat3, mat4)
            simfuncs.changing(mat1, mat3, mat4)
            simfuncs.gens(mat2, mat3)
            simfuncs.recovery(mat3, mat4, mat2)
            simfuncs.stats(mat2)
            mat1 = mat2

            for y in range(len(mat1)):
                print(mat1[y]),
            print(" ")

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

        if simvars.gencount % 2 == 0:
            popinfec = 0
            for y in range(len(mat2)):
                for x in range(len(mat2[y])):
                    if mat2[y][x] == simvars.infec or mat2[y][x] == simvars.rest:
                        popinfec += 1
            data[simvars.gencount] = popinfec

        else:
            popinfec = 0
            for y in range(len(mat2)):
                for x in range(len(mat2[y])):
                    if mat2[y][x] == simvars.infec or mat2[y][x] == simvars.rest:
                        popinfec += 1
            data[simvars.gencount] = popinfec

    genlis = list()
    numforgen = list()
    for k, v in data.items():
        genlis.append(k)
        numforgen.append(v)

    plt.plot(genlis, numforgen)


main()
