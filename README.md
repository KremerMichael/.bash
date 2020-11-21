Note that the symbolic link in this repo expects this directory to be located ~/.bash
To add these functions to the bash shell, add this section to your ~/.bashrc






```sh
#=================================================================================================#
# BASH SOURCE
#=================================================================================================#
#Source bash shell from .bash/ 
if [ -f ~/.bash/bash_source ]; then
   . ~/.bash/_env
fi
```sh
