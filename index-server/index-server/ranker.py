#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    ranker.py - Matches the query against the saved indexed chunks and returns a list of dictionaries with docID
    author: Pablo Caruana
    email: pablo dot caruana at gmail dot com
    date: 12/1/2016

"""

import math

def term_frequency_weighting(tf):
    return 1 + math.log10(tf)

def inverse_document_frequency_weighting(N, df):
    return math.log10(N/df)
