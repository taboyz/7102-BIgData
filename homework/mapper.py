# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:12:05 2018

@author: kronprom
"""

#!/usr/bin/env python

from operator import itemgetter
import sys

if __name__ == '__main__':
        for line in sys.stdin:
            for word in line.split():
                sys.stdout.write('{0}\t1\n'.format(word))    
            