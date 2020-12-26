#=================================================================================================#
# BASH SOURCE
# Source bash shell from .shell/ 
#=================================================================================================#
#This path needs to manually set
export SHELL_PATH='/Users/kremerme/.shell'
if [ -f $SHELL_PATH/_env ]; then
    . $SHELL_PATH/_env
fi
