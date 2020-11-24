#!/usr/bin/env python3
################################################
# The purpose of this function is to recursively
# push git sub-directories from the lowest child
# back to the top
################################################
# Imports
import os
import argparse
import subprocess
# Defines
DEBUG=True

def git_recursive(path):
    if DEBUG:
        print("git_recursive started at {}".format(path))

    # Try to open <path>/.gitmodules
    gitmodules_path = os.path.join(path, ".gitmodules")
    if os.path.exists(gitmodules_path):
        gitmodules_file = open(gitmodules_path, "r")
        lines = gitmodules_file.readlines()

        for line in lines:
            line = line.strip()
            # Parse for submodules
            if line[0] == '[':
                if DEBUG:
                    print("submodule detected: {}".format(line))
                else:
                    x=0 # See what happens with a pass here
            elif line[0] == 'p':
                path_submodule_relative = line[7:]
                path_submodule_absolute = os.path.join(path, path_submodule_relative)
                if DEBUG:
                    print("path to submodule {}".format(path_submodule_absolute))
                git_recursive(path_submodule_absolute)
        subprocess.run('/home/kremerme/.bash/bin/git_wrapper -p')
    else:
        git_path = os.path.join(path, ".git")
        if DEBUG:
            print("No {} found, checking for {}".format(gitmodules_path, git_path))
        if os.path.exists(git_path):
            if DEBUG:
                print("pushing from {}".format(path))
            print("TODO, implement push")
        else:
            if DEBUG:
                print("ERROR: Not inside of git repository")
            x=0 # See what happens with a pass here
                    
################################################
# MAIN 
################################################
#if __name__ == "__main":
    ################################################
    # SET UP ARGUMENTS
    ################################################
parser = argparse.ArgumentParser(description='A function build to recursively push nested git repos, child->parent')
parser.add_argument('-p', '--path', help='path to parent directory')
arguments = parser.parse_args()
if arguments.path is None:
    path = os.getcwd()
else:
    path = arguments.path

################################################
# START
git_recursive(path)
################################################
# END
print('DONE')
################################################
