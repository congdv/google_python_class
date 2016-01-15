#!/usr/bin/python2.7
import sys
def read_file(file_name):
    word_count = {}
    f = open(file_name,'r')
    for line in f:
        words = line.rstrip('\n').split(' ')
        for word in words:
            if word not in word_count.keys():
                word_count[word] = 1
            else:
                word_count[word] = word_count[word] + 1
    for word in sorted(word_count):
        print word + ' %d'%word_count[word]
def main():
    if len(sys.argv) == 2:
        read_file(sys.argv[1])
    else:
        read_file('blogger.txt')

if __name__ == '__main__':
    main()
