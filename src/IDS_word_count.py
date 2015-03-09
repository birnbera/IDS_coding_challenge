# -*- coding: utf-8 -*-
import string
import fileinput

# Create concatenated file object from files listed in arguments
fileargs1 = fileinput.input()
fileargs2 = fileinput.input()

def word_count(fileargs):
    '''Returns word counts from a text stream as a list of tuples.'''
    countdict = {}
    for line in fileargs:
        line = line.strip().split()
        for word in line:
            word = word.lower()
            word = word.translate(None, string.punctuation + string.digits)
            if word in countdict:
                countdict[word] += 1
            else:
                countdict[word] = 1
    return sorted(countdict.items(), key=lambda x: x[0])

def word_median(fileargs):
    '''Returns streaming median number of words per line in text stream.'''
    counts = []
    for line in fileargs:
        line = line.strip().split()
        counts.append(len(line))
        counts.sort()
        ncounts = len(counts)
        mid = ncounts/2  # Floor integer division
        if ncounts % 2 == 0:
            yield sum(counts[mid-1:mid+1])/2.0
        else:
            yield counts[mid]

wordcounts = word_count(fileargs1)

'''for w, c in wordcounts:
    print '%s%i' % (w.ljust(12), c)'''

with open('wc_output/wc_result.txt', 'w') as wc_out:
    for w, c in wordcounts:
        wc_out.write('%s%i\n' % (w.ljust(12), c))

wordmedians = word_median(fileargs2)

'''for count in wordmedians:
    print '%.1f' % count'''

with open('wc_output/med_result.txt', 'w') as med_out:
    for count in wordmedians:
        med_out.write('%.1f\n' % count)

fileargs1.close()
fileargs2.close()
