#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test the search module
"""
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import pytest
import logging

from profilers.boyer_moore import string_search
from profilers.pigeonhole import approximate_match


def test_boyer_moore():
    pattern = 'TGGATGTGAAATGAGTCAAG'
    testText = 'CGCTAAAAGCTAGAGCTACGCGACGATCAGCACTACGTGGATGTGAAATGAGTCAAGCGCGCTAGACGACTACGACTAGCAGCATCGATCGATCGATCG'
    result = string_search(pattern=pattern, text=testText)
    assert result == [37]


def test_approximate_matching():
    switchMap = {"A": "G", "C": "A", "G": "T", "T": "G"}
    text = 'CACTTAATTTG'
    textList = [value for value in text]
    pattern = text[:6]
    patternList = [value for value in pattern]
    first_mismatch_index = 0
    patternList[first_mismatch_index] = switchMap[textList[first_mismatch_index]]
    second_mismatch_index = 5
    patternList[second_mismatch_index] = switchMap[textList[second_mismatch_index]]
    pattern = ''.join(patternList)
    text = ''.join(textList)
    indices = approximate_match(pattern=pattern, text=text, max_allowed_mismatches=2)
    assert indices == [first_mismatch_index, second_mismatch_index]
    # pattern = 'AACTTG'

