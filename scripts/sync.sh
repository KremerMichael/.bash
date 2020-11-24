#store apt list
#TODO, check that sys is ubuntu
rm ~/sys/apt_list.txt
apt list >> ~/sys/apt_list.txt

#sync all of git
cd ~/
echo "WIP git recursive"
#git_wrapper -r
