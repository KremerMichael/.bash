# Get date so we can time stamp files
date=$(date +"%m-%d-%y")

# Store lists
if [ $MACHINE = linux ]; then
    #TODO check for arch vs ubuntu
    # Remove old list
    rm $SHELL_PATH/etc/apt_list_*.txt
    # Write new list
    apt list > $SHELL_PATH/etc/apt_list_$date.txt

elif [ $MACHINE = mac ]; then
    # Remove old list
    rm $SHELL_PATH/etc/brew_list_*.txt
    # Write new list
    brew list --formula > $SHELL_PATH/etc/brew_list_$date.txt
fi

# sync up some rc files
if [ -f ~/.bashrc ]; then 
    cp ~/.bashrc $SHELL_PATH/etc/ 
fi
if [ -f ~/.vimrc ]; then
    cp ~/.vimrc $SHELL_PATH/etc/
fi


