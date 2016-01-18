#!/usr/bin/python2.7
import re
import sys
import time
def values(word_count):
    return word_count[1]
def read_file(file_name,sorted_count=False):
    word_count = {}
    f = open(file_name,'r')
    for line in f:
        words = line.rstrip('\n').split(' ')
        for word in words:
            word = re.search('[a-zA-Z]+',word)
            if word:
                word = word.group()
                if word not in word_count.keys():
                    word_count[word] = 1
                else:
                    word_count[word] = word_count[word] + 1
    if sorted_count:
        for word,count in sorted(word_count.items(),key=values,reverse=True):
            print word +' %d'%count

    else:
        for word in sorted(word_count):
            print word + ' %d'%word_count[word]
def main():
    if len(sys.argv) == 2:
        read_file(sys.argv[1])
    elif len(sys.argv) == 3:
        if sys.argv[1] == '--topcount':
            read_file(sys.argv[2],True)
        else:
            print 'False input'
    else:
        read_file('blogger.txt')

if __name__ == '__main__':
    main()
