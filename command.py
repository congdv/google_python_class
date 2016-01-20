#!/usr/bin/python2.7

import sys
import commands
import os
import re
def count_file(dir):
    _file=[]
    filenames = os.listdir(dir)
    print len(filenames)
    for filename in filenames:
        if re.search(r'.+\..+',filename):
            _file.append(filename)
    return _file
def Command(cmd,dir1=None,dir2=None):
    if cmd == 'ls -l ':
        command = cmd + dir
    elif cmd == 'cp ':
        command = cmd + "%s %s" %(dir2,dir1)
    elif cmd == 'zip ':
        command = cmd + "-r %s %s"%(dir1,dir2)
    print 'command : %s'%command
    (status,output) = commands.getstatusoutput(command)
    if status:
        sys.stderr.write( "error %s"%status)
    else:
        print output

def main():
    try:
        cmd = None
        if len(sys.argv) == 2:
            cmd = 'ls -l '
            dir = sys.argv[1]
            Command(cmd,dir)
        elif len(sys.argv) == 4:
            if sys.argv[1] == '--todir':
                cmd = 'cp '
                dirs = []
                if sys.argv[3] == '.' or  sys.argv[3] == './':
                    dirs = count_file('.')
                else:   dirs.append(sys.argv[3])
                for d in dirs:
                    Command(cmd,sys.argv[2],d)
            elif sys.argv[1] == '--tozip':
                cmd = 'zip '
                dirs = []
                if sys.argv[3] == '.' or  sys.argv[3] == './':
                    dirs = count_file('.')
                else:   dirs.append(sys.argv[3])
                print dirs
                for d in dirs:
                    Command(cmd,sys.argv[2],d)
        else:
            print "usage:[--todir dir][--tozip zipfile] dir dir dir"
    except:
        sys.stderr.write("Error format \n")
        sys.exit(1)
if __name__ == '__main__':
    main()
