#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Profile the Matcher Module
"""
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import bisect


class Index:
    def __init__(self, text, k):
        self.k = k
        # self.index = []
        # for i in range(len(text) + 1):
        #     self.index.append((text[i:i+k], i))
        self.index = [(text[i:i+k], i) for i in range(len(text) + 1)]
        self.index.sort()

    def query(self, pattern):
        kmer = pattern[:self.k]
        #  find first position in the list where this kmer occurs
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        #  return all the indices in the Text where the first k bases of the pattern matches
        return hits


def query_index(pattern, text, index):
    # return list of offsets
    return [i for i in index.query(pattern) if pattern[index.k:] == text[i+index.k:i+len(pattern)]]


def example():
    text = 'GCTACGATCTAGAATCTA'
    pattern = 'TCTA'
    index = Index(text=text, k=2)
    print(query_index(pattern=pattern, text=text, index=index))
