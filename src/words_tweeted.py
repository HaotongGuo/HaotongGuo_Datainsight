""" Insight Data Challenge
    This file calculates the total number of times each word has been tweeted.
    Done By: Haotong Guo
"""
import sys

#Open file for read and extract all tweet, then count the word occurance among all the tweets, save the result into output file
#input:input file(contain tweets), output file
def words_tweet(filename, outname):
    file = open(filename, 'r')
    #initialize the dictionary for word:occurance pair
    countword = dict()
    for line in file:
        line = line.rstrip()
        words = line.split()
        for word in words:
                countword[word] = countword.get(word,0)+1
    #sort result based on word
    lst = countword.items()
    lst.sort()
    #write result into output file
    output1 = open(outname,'w')
    cnt  = 0
    for key, val in lst:
        cnt  = cnt + 1
        if cnt == 1:
            output1.write(key+str(val).rjust(29 - len(key)))
        else:
            output1.write('\n'+key+str(val).rjust(29 - len(key)))
    output1.close()

def main():
    #input file read from command
    filename = sys.argv[1]
    #output file read from command
    outname = sys.argv[2]
    words_tweet(filename, outname)

main()