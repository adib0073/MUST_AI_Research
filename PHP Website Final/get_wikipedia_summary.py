# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 15:11:57 2018

@author: aaygupta
"""
import wikipedia
import sys
import string

filter_data = ''
printable = set(string.printable)

def get_summary(search_term = 'Satya Nadella'):
    _summary = wikipedia.summary(search_term)
    _paragraph = _summary.splitlines()
    print(_paragraph[0])
    _test = filter(lambda x: x in printable, _paragraph)
    print(''.join(_test))
    #return _summary
    file = open("summary.txt", "w") 
    file.write(str(_paragraph))
    file.close() 
    print("Success")
 
 
if __name__ == "__main__":
    keyword = str(sys.argv[1])
    get_summary(keyword)