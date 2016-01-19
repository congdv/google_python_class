#!/usr/bin/python2.7
import re
from sys import argv

def values(items):
    return items[1]
def read_file(file_name):
    f = open(file_name,'r')
    return f.read()
def find_title(content):
    match = re.search(r'<th><h1>(.*2014)</h1></th>',content)
    if match:
         return match.group(1)
    return None
def find_name(content):
    baby_names = {}
    match = re.findall(r'<td>(.+)</td>.*<td>(.+)</td>.*<td>(.+)</td>',content)
    if match:
        for name in match:
            baby_names[name[1]] = name[0]
            baby_names[name[2]] = name[0]
    return baby_names
def print_ranked(names,default=True):
    if default:
        for name in sorted(names):
            print name + ' %s'%names[name]
    else:
        for name in sorted(names.items,key=values):
            print name[0] + ' %s'%name[1]
def argv_input():
    if len(argv) == 1:
        return 1
    elif len(argv) == 3:
        return 2
    else:
        return 3
def write_file_name(names,file_name):
    f = open(file_name,'w')
    for name in sorted(names):
        f.write(name + " %s\n"%names[name])
    f.close()
def help():
    print "HELP: 2 argument: file name for read,file name format for write \n 0 argument: for print default count "
def main():
    _input = argv_input()
    if _input == 1:
        help()
        return
    elif _input == 2:
        file_name = argv[1]
        ext = argv[2]
        content = read_file(file_name)
        baby_names = find_name(content)
        write_file_name(baby_names,file_name+"."+ext)
    else:
        file_name = "babyname2014.html"
        content = read_file(file_name)
        baby_names = find_name(content)
        print_ranked(baby_names)
if __name__ == '__main__':
    main()
