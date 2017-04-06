#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PCL II, Übung 4, FS17
# Aufgabe 2
# Autor: Nora Lötscher & Alex Flückiger
# Matrikel-Nr.: 09-110-552 & 12-452-223

"""
Script extracts random elements into output file and writes rest into another file.
"""

import random

def gettitles(infile, testfile, trainfile, k):
	# infile is corpus
	# testfile is output file with k randomly selected titles
	# trainfile is output file with rest of titles
	
	"""
	Reservoir Sampling:
	
	reservoir = []
	for t, item in enumerate(iterable):
		if t < k:
			reservoir.append(item)
		else:
			m = random.randint(0,t)
			if m < k:
				reservoir[m] = item
	return reservoir
	"""

# iterate through xml file and build lemmatised sentences out of word lemmas
# find 20 most frequent sentences that are AT LEAST 6 TOKENS LONG (write into output file)

def main():
    gettitles()


if __name__ == '__main__':
    main()