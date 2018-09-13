#!/usr/bin/env python

from operator import itemgetter
import sys

if __name__ == '__main__':
        for line in sys.stdin:
            count = 0
            for word in line.split():
                count += 1
                if count%2 == 1:
                    word1 = word
                else:
                    word2 = word
                #print ('{0} {1}\t1\n'.format(word1,word2)
                sys.stdout.write('{0} {1}\t1\n'.format(word1,word2)) 
            
       
       
       
#with open ("text.txt", "r") as myfile:
#    for line in myfile:
#        count = 0
#        for word in line.split():
#            count += 1
#            print (count)
#            if count%2 == 1:
#                word1 = word
#            else:
#                word2 = word
#                print ('{0} {1}\t1\n'.format(word1,word2))
                