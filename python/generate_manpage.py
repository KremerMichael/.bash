#!/usr/bin/env python3
################################################
# The purpose of this function is to create a 
# man page given any python file
# TODO get this working for bash and others
################################################
import os
import sys
import argparse
import subprocess
# Defines
# NONE


################################################
# SET UP ARGUMENTS
################################################
parser = argparse.ArgumentParser(description='A function build to recursively push nested git repos, child->parent')
parser.add_argument('-f', '--file', help='File used to create manpage')
args = parser.parse_args()


################################################
# MAIN 
################################################
# get file
if args.file:
    print("wjat")
    _file = open(args.file, 'r')
else:
    print("ERROR: No file specified")
    print("TODO: print argparse")
    sys.exit(1)

# read lines
lines = _file.readlines()
for line in lines:
    print(line)
    

# interpret my standard header
# interpret argparse
