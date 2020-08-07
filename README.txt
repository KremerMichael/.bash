In order to add these functions to the bash shell, add this section to your ~/.bashrc

#=================================================================================================#
# BASH
#=================================================================================================#
#Store alias definitions in ~/.bash/bash_aliases and load them with this
if [ -f ~/.bash/bash_aliases ]; then
    . ~/.bash/bash_aliases
fi

#Store function definitions in ~/.bash/bash_functions and load them with this
if [ -f ~/.bash/bash_functions ]; then
    . ~/.bash/bash_functions
fi

#Store destinations for ssh in ~/.bash/bash_ssh
if [ -f ~/.bash/bash_ssh ]; then
    . ~/.bash/bash_ssh
fi

# enable programmable completion features
if ! shopt -oq posix; then
    if [ -f /usr/share/bash-completion/bash_completion ]; then
	. /usr/share/bash-completion/bash_completion
    elif [ -f /etc/bash_completion ]; then
	. /etc/bash_completion
    fi
fi
#=================================================================================================#

Note that bash_ssh is ignored in the git repo:
It's probably smart to not host ssh usernames and destinations remotely

Also note that the symbolic link in this repo expects this directory to be located ~/.bash
