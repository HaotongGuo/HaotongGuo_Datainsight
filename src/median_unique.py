""" Insight Data Challenge
    This file calculates the median number of unique words per tweet, and update this median as tweets come in.
    Done By: Haotong Guo
"""
import sys
import bisect

#calculate median value in a list, the median of a set with an even number of items is the mean of the two middle elements
#input:list
#output:median value
def median(l):
    if len(l)%2 == 0:
        return float(l[len(l)/2]+l[len(l)/2-1])/2
    else:
        return l[(len(l)-1)/2]

#Open file for read and extract all tweet, count unique word occurance in each tweet, store new coming count in list in ascending order,update median value, and save the result into output file
#input:input file(contain tweets), output file
def median_unique(filename, outname):
    file = open(filename, 'r')
    #initialize the list for storing unique word count for each tweet
    unique = list()
    #initialize the list for median after each update
    medlst = list()
    for line in file:
        countword = dict()
        line = line.rstrip()
        words = line.split()
        for word in words:
            countword[word] = countword.get(word,0)+1
        num = len(countword.keys())
    #using bisect to insert new count to keep the list in order, which improves efficiency on finding the median value(no need do entire list sorting every time)
        bisect.insort_left(unique,num)
        medlst.append(median(unique))
    #write result into output file
    output2 = open(outname,'w')
    for val in medlst:
            output2.write("%s\n" % val)
    output2.close()

def main():
    filename = sys.argv[1]
    outname = sys.argv[2]
    median_unique(filename,outname)

main()