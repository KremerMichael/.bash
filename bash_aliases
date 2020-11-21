#!/usr/bin/env bash
#=================================================================================================#
# ALIASES
#=================================================================================================#

#Emacs typos
alias emasc='emacs'
alias emcas='emacs'
alias emcsa='emacs'

#Python
alias python='python3.8'

#Lauching doom, i.e.
alias doom='emacs'

#Some ls aliases
alias sl='ls'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

#to run eagle
alias eagle='~/Public/eagle-9.6.2/eagle'

#to run Citrix Desktop app
alias citrix='/opt/Citrix/ICAClient/selfservice'

#for automated git_push
alias gp='git_push'

#Shorten tilde function
alias ct='clean_tilde'

#todo alias
alias td='todo'

#Confirm before overwriting something
alias cp="cp -i"

#cd shortcuts
alias c.="cd ../"
alias c2="cd ../../"
alias c3="cd ../../../"
alias c4="cd ../../../../"

#human-readable sizes
alias df='df -h'

#Check mem of home directory
alias home_mem='du -shc *'

#Add an "alert" alias for long running commands.  Use like so:
#example: sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
