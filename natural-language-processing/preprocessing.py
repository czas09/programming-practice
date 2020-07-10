"""Common preprocessing utilities for working with text"""
import re
import heapq
import os.path as op
from collections import Counter

import numpy as np


_STOP_WORDS = {}
_PUNCTUATION = ""
_WORD_REGEX = re.compile(r"")
_PUNC_TABLE = str.maketrans("", "", _PUNCTUATION)


def ngrams(sequence, N):
    pass


def tokenize_words(line, lowercase=True, filter_stopwords=True):
    pass


def tokenize_chars(line, lowercase=True, filter_punctuation=True):
    pass


def remove_stop_words(words):
    pass


def strip_punctuation(line):
    pass


# Huffman Tree =============================================

class Node(object):
    pass


class HuffmanEncoder(object):
    pass


# Containers ===============================================

class Token:
    pass


class TFIDFEncoder:
    pass


class Vocabulary: 
    pass