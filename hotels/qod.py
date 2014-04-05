#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: silver
# @Date:   2014-04-03 20:22:54
# @Last Modified by:   silver
# @Last Modified time: 2014-04-06 01:19:42
#
# This module contains useful functions to ensure Quality of Data and data treatment.
from datetime import date
from pprint import pprint

five = ['rooms', 'location', 'cleaning', 'reception', 'others']
ten = ['general', 'price', 'restaurant']

# Reads ratings from dictionary input and checks for range validty 0-10 and 0-5
def checkRatings(dictio, debug):
    if debug:
        irate = sum(len(r) for r in [v for v in dictio.itervalues()])     
    for hotel in dictio.keys():
        for rating in dictio[hotel].keys():
            if len(dictio[hotel][rating]) > len(__checkRate(dictio[hotel][rating])):
                del dictio[hotel][rating]
    if debug:        
        with open(debug, 'a') as d:
            arate = sum(len(r) for r in [v for v in dictio.itervalues()])
            d.write("------------ QOD --------------\n")
            d.write("Checked {} rates, deleted {}. Integrity {}%\n".format(irate, irate-arate, (float(arate)/irate)*100))
            d.write("-------- {} ---------\n\n".format(date.today().strftime('%c')))

def __checkRate(rating):
    for rate in rating.keys():
        if rating[rate] < 0:
            del rating[rate]
            continue
        if rate in five:
            if rating[rate] > 5:
                del rating[rate]
                continue
        if rate in ten:
            if rating[rate] > 10:
                del rating[rate]
                continue
    return rating

def avarageRating(dictio):
    avarageRatings = {}
    for hkey, hvalue in dictio.iteritems():
        rates = len(hvalue)
        avarageRatings[hkey] = {}
        for rkey, rvalue in hvalue.iteritems():
            for key, value in rvalue.iteritems():                
                if key not in avarageRatings[hkey]:
                    avarageRatings[hkey][key] = 0
                avarageRatings[hkey][key] += value        
        for key, value in avarageRatings[hkey].iteritems():
            avarageRatings[hkey][key] = value/rates
    return avarageRatings
