#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: UOC
# @Date:   2014-04-03 20:00:13
# @Last Modified by:   silver
# @Last Modified time: 2014-04-05 21:43:52

# Produces a sorted list of global ratings from a dictionary of
# user ratings, in the form
# [(movieId, globalRating)]
def meanGlobalRatings(dictio):
    # Auxiliary dictionary {movieId: [ratings]}
    aux = {}
    for userValue in dictio.values():
        for movieId in userValue:
            if not aux.has_key(movieId):
                aux[movieId] = []
            aux[movieId].append(userValue[movieId])                

    # Compute and sort global ratings
    mean   = lambda x: sum(x)/float(len(x))
    result = [(p, mean(aux[p])) for p in aux]
    result.sort(key = lambda x: x[1], reverse=True)
    return result

