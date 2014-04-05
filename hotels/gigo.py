#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: silver
# @Date:   2014-04-03 20:28:01
# @Last Modified by:   silver
# @Last Modified time: 2014-04-05 01:58:05
# This module contains useful functions to process data input/output.
import re
from datetime import date
# Reads ratings from data fileinput and returns a dictionary with key=values
# Ensure each line of file has its expected format, if there is a malformed line it
# is skiped and debuged if a path is provied.
def readRatings(filename, debug=False):    
    dictio = {}
    lines = 0
    with open(filename, 'r') as f:
        for l in (f.readlines()):            
            lines +=1
            rate = re.match('(\d+)\t(\d+)\t(\d+)\t(\d+)\t(\d+)\t(\d+)\t(\d+)\t(\d+)\t(\d+)\t(\d+)', l)            
            if rate:
                if not int(rate.group(1)) in dictio:
                    dictio[int(rate.group(1))] = {}
                dictio[int(rate.group(1))][int(rate.group(2))] = {
                    'general' : int(rate.group(3)),
                    'rooms' : int(rate.group(4)),
                    'location' : int(rate.group(5)),
                    'cleaning' : int(rate.group(6)),
                    'price' : int(rate.group(7)),
                    'reception' : int(rate.group(8)),
                    'restaurant' : int(rate.group(9)),
                    'other' : int(rate.group(10))
            }
    if debug:
        with open(debug, 'a') as d:
            d.write("\n------------ Import --------------\n")
            d.write("Read {} lines from file {}\n".format(lines, filename))
            succ = sum(len(v) for v in dictio.itervalues())
            d.write("Imported {} hotels with {} ratings. ({}%)\n".format(len(dictio), succ , (succ/lines)*100))
            d.write("-------- {} ---------\n\n".format(date.today().strftime('%c')))
    return dictio