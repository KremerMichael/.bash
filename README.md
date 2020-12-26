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
#=============================================================================#
# BASH SOURCE
#=============================================================================#
#Source bash shell from .shell/ 
if [ -f ~/.shell/_env ]; then
   . ~/.shell/_env
fi
```

# Contact Me

Michael Kremer, <kremeremichael@gmail.com>
