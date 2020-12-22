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
import datetime
# Defines
# NONE


################################################
# SET UP ARGUMENTS
################################################
parser = argparse.ArgumentParser(description='A function build to auto-generate manpages for given functions', add_help=False)
parser.add_argument('-f', '--file', help='File used to create manpage')
parser.add_argument('-v', '--verbose', help='enable more verbose printing')
parser.add_argument('-V', '--very-verbose', help='verbose + print lines as written to file')
parser.add_argument('-h', '--help', help='help')
args = parser.parse_args()


################################################
# MAIN 
################################################
# get file
if args.file:
    function_name = args.file.split('.')[0]
    extension = args.file.split('.')[1]
    _file = open(args.file, 'r')
else:
    print("ERROR: No file specified")
    parser.print_help()
    sys.exit(1)

# read lines
lines = _file.readlines()
for line in lines:
    if extension == 'py':
        pass
    elif extension == '.sh':
        pass

# Open file
manpage = open(function_name + ".1", "w")

# Write preamble
manpage.write('.\\"\n')
manpage.write('.\\" Man page for {}\n'.format(function_name))
manpage.write('.\\"\n')
manpage.write('.\\" {} {}\n'.format(os.getenv('FIRST_NAME'),os.getenv('LAST_NAME')))
manpage.write('.\\" {}\n'.format(os.getenv('EMAIL')))
manpage.write('.\\" Electrical Engineer\n')
manpage.write('.\\" {}\n'.format(os.getenv('EMPLOYMENT')))
manpage.write('.\\"\n')
manpage.write('.\\" Automatically generatedy by generate_manpage.py\n')

# Write lead line
current_date = datetime.datetime.today()
month = current_date.strftime('%B')
manpage.write('.TH {} "{} {}, {}"\n'.format(function_name, month, current_date.day, current_date.year))
manpage.write('.LO 1\n')

# Write name
manpage.write('.SH NAME\n')
manpage.write('{} \\- TODO put short description here\n'.format(function_name))

# Write synopsis
manpage.write('.SH SYNOPSIS\n')
manpage.write('.B {}\n'.format(function_name))
#TODO arguments here
manpage.write('')

# Write description
manpage.write('.SH DESCRIPTION\n')
manpage.write('.B {}\n'.format(function_name))
#TODO figure out description
manpage.write('')

# Write options
manpage.write('.SH OPTIONS\n')
for option in options:
    manpage.write('.TP\n')
    #TODO write argument flag
    #TODO write description of argument
manpage.write('')

# Write author
manpage.write(".SH  AUTHOR\n")
manpage.write("{} {} <{}>.".format(os.getenv('FIRST_NAME'), os.getenv('LAST_NAME'), os.getenv('EMAIL')))

#Done
manpage.close()
