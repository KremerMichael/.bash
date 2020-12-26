<div align="center">

# Greetings!

</div>

Hello and welcome to my shell! 

### Table of Contents
- [Introduction](#introduction)
- [Overview](#overview)
- [Install](#install)
- [Contact Me](#contact-me)

# Introduction

This repo is a representation of my love for the shell. 

# Overview

**bin/**

A collection of bash functions. This directory is added to the $PATH by \_env

**etc/**

Config files, some files in this directory are synced with pre-hook scripts

**MAN/**

Man pages I have either written or generated for the scripts and functions in
this repo.

**templates/**

Really a work in progress, but it's nice to have a collection of templates for
varius types of files. 

**python/**

A collection of python functions. Currently working on setting this up inside
of a virtual enviornment.

**scripts/**

A collection of scripts that not used often enough to be include in a directory
appeneded to $PATH.

# Install

To add these functions to the bash shell, add this section to your ~/.bashrc

```sh
#=================================================================================================#
# BASH SOURCE
# Source bash shell from .shell/ 
#=================================================================================================#
#This path needs to manually set
export SHELL_PATH='/Users/kremerme/.shell'
if [ -f $SHELL_PATH/_env ]; then
    . $SHELL_PATH/_env
fi
```

Note that the above sourcing assumes .shell/ is located inside of the home 
directory. If .shell/ is not checked out into the home directory, the path 
above will have to be changed appropriately.

# Contact Me

Michael Kremer, <kremeremichael@gmail.com>
