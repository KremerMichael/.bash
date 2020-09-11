#!/usr/bin/env bash
#=================================================================================================#
# USEFUL FUNCTIONS
#=================================================================================================#
#Send a DM to myself on apollotool Slack
#usage: notify-slack <message>
notify-slack() {
    msg=$1 #grab first input
    echo $1
    data='{"text" : "'"$msg"'"}'
    SLACK_MESG="curl -X POST -H 'Content-type: application/json' --data '${data}' https://hooks.slack.com/services/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"
    echo $SLACK_MESG | bash >& /dev/null
}

#Run Vivado IDE
vivado_gui() {
    source /opt/Xilinx/Vivado/2019.2/settings64.sh
    vivado
    clean_vivado
}

#Read from todo list
todo() {
    clear
    cat ~/Documents/toDo.txt
}

todo_edit() {
    emacs ~/Documents/toDo.txt -nw
}

git_config() {
    git config --global user.email $EMAIL
    git config --global user.name  $GIT_USERNAME
}

#Archive extractor
#usage: ex <file>
ex () {
    if [ -f $1 ] ; then
	case $1 in
	    *.tar.bz2)   tar xjf $1    ;;
	    *.tar.gz)    tar xzf $1    ;;
	    *.bz2)       bunzip2 $1    ;;
	    *.rar)       unrar x $1    ;;
	    *.gz)        gunzip $1     ;;
	    *.tar)       tar xf $1     ;;
	    *.tbz2)      tar xjf $1    ;;
	    *.tgz)       tar xzf $1    ;;
	    *.zip)       unzip $1      ;;
	    *.Z)         uncompress $1 ;;
	    *.7z)        7z x $1       ;;
	    *)           echo "'$1' cannot be extracted via ex()" ;;
	esac
    else
	echo "'$1' is not a valid file"
    fi
}

#Display system colors
colors() {
    local fgc bgc vals seq0

    printf "Color escapes are %s\n" '\e[${value};...;${value}m'
    printf "Values 30..37 are \e[33mforeground colors\e[m\n"
    printf "Values 40..47 are \e[43mbackground colors\e[m\n"
    printf "Value  1 gives a  \e[1mbold-faced look\e[m\n\n"

    # foreground colors
    for fgc in {30..37}; do
        # background colors
        for bgc in {40..47}; do
            fgc=${fgc#37} # white
            bgc=${bgc#40} # black

            vals="${fgc:+$fgc;}${bgc}"
            vals=${vals%%;}

            seq0="${vals:+\e[${vals}m}"
            printf "  %-9s" "${seq0:-(default)}"
            printf " ${seq0}TEXT\e[m"
            printf " \e[${vals:+${vals+$vals;}}1mBOLD\e[m"
        done
        echo; echo
    done
}

#push changes to current branch to origin
#usage: git_push <commit message>
git_push() {
    #removing tildes because they are insanely annoying
    clean_tilde

    #Getting message from user
    msg=$1
    [ -z "$1" ] && msg="auto push run at $(date)" #if no message send date of auto push
    #echo $msg

    #add all changes
    git add .
    #Get current branch
    branch=$(git rev-parse --abbrev-ref HEAD)
    #Commit and push to origin branch 
    git commit -m "$msg"
    git push -u origin $branch
}

status() {
    git status > /tmp/tmp.txt
    if [ $? = 0 ]
   then
    cat /tmp/tmp.txt
    else
    svn status > /tmp/tmp.txt
    if [ $? = 0 ]
   then
    cat /tmp/tmp.txt
    else
    echo "Not in git or svn repo"
    fi
    fi
}
#=================================================================================================#
# HOUSE-KEEPING
#=================================================================================================#
#Remove all files ending with tilde
clean_tilde() {
    rm ./*~ &> /dev/null
    rm ./.*~ &> /dev/null
    rm ./#*# &> /dev/null
}

#Remove log files from vivado
clean_vivado() {
    rm ./vivado.jou
    rm ./vivado.log
}


