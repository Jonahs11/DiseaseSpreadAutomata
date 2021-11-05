#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:47:10 2020

@author: jonah
"""
#placeholder values in matrix
posplace = 99
pospos = 90

#size of matrix
length = 20
#total number of generations
numgens = 20

#designated states for an individual
uninfec = 0
infec = 1
rest = 2

ci1 = .1
ci2 = .2
ci3 = .3
ci4 = .4
ci5 = .5
ci6 = .6
ci7 = .7
ci8 = .8

#proportion of the population that starts infected
startinginfec =.05

#6 potential incubation times for an infected individual
it1 = -2
it2 = -3
it3 = -4
it4 = -5
it5 = -6
it6 = -7

#probabilites for having a given incubation time
incubr1 = .2
incubr2 = .4
incubr3 = .6
incubr4 = .8
incubr5 = 1.0


#probability for given recovery times
rr1 = 0.2
rr2 = 0.4
rr3 = 0.6
rr4 = 0.8
rr5 = 1.0

#different recovery times
rt1 = -2
rt2 = -3
rt3 = -4
rt4 = -5
rt5 = -6

start = 0
gencount = 0

data = dict()
