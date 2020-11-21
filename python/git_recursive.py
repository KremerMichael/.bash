#!/usr/bin/env python3
################################################
# The purpose of this function is to recursively
# push git sub-directories from the lowest child
# back to the top
################################################
#imports
import os
import argparse
#generics
debug=True

################################################

def git_recursive():
    #Get absolute current path
    current_path=os.getcwd()
    if debug:
        print("top path: " + str(current_path))

    #Try to open ./.gitmodules
    gitmodules_path = os.path.join(current_path, ".gitmodules")
    try:

        if debug:
            print("trying to open: " + str(gitmodules_path))

        gitmodules_file = open(gitmodules_path, "r")
        lines = gitmodules_file.readlines()

        for line in lines:
            line = line.strip()
            #Parse for submodules
            if line[0] == '[':
                print("submodule detected: " + str(line))
            #Parse for paths
            if line[0] == 'p':
                print("path to submodule: " + line[7:])
                relative_path = line[7:]
                os.chdir(relative_path)
                git_recursive()

    except:
        git_path = os.path.join(current_path, ".git")
        print("No " + str(gitmodules_path) + " found, checking for " + str(git_path))
        if os.path.exists(git_path):
            print("time to push")
        else:
            print("ERROR: Not inside of git repository")


if __name__ == "__main__":
    git_recursive()
    print("DONE")
