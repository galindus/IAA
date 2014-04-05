#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: silver
# @Date:   2014-04-03 23:20:50
# @Last Modified by:   silver
# @Last Modified time: 2014-04-06 01:11:58
from hotels import *
from uoclib import *
from sklearn.metrics.cluster import adjusted_rand_score
from pprint import pprint


def __adjusted_rand_index(generated):
    # generate expected assignment array.
    expected = []
    for x in range(4):
        for y in range(5):
            expected.append(x)
    predicted = [x for x in generated.itervalues()]
    pprint(predicted)
    pprint(expected)
    return adjusted_rand_score(expected, predicted)

    

if __name__ == "__main__":
    # Get dictionary of data.
    dictio = gigo.readRatings("data/hotels.data", "data/input.debug")
    # Ensure Quality of Ratings.
    qod.checkRatings(dictio, "data/input.debug")
    # Generate avarages for each hotel.
    avarageDict = qod.avarageRating(dictio)
    # Generate k-means 4
    dictout = kmeansDictio.kmeans_dictio(avarageDict, 4, 100, kmeansDictio.pearsonCoeff)
    # Expected
    #expected = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
     #= adjusted_rand_score(dictout[0], expected)
    pprint(dictout)
    test = __adjusted_rand_index(dictout[0])
    pprint(test)

