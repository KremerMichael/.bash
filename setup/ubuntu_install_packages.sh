#=============================================================================================================
# This script installes all of the packages configured in packages.cfg for an Ubuntu Linux distribution. The
# only dependency of this script is 'apt' which should be included already in any reasonable Ubuntu
# distribution
#=============================================================================================================

# SETUP
sudo apt update
if [ -f ~/Scripts/setup/packages.cfg ]; then . ~/Scripts/setup/packages.cfg || echo "ERROR loading packages.cfg"; fi
#=============================================================================================================

# CODE DEVELOPMENT
if [ $en_gcc = yes ];      then sudo apt install gcc || echo "Failed installing gcc"; fi
if [ $en_g++ = yes ];      then sudo apt install g++ || echo "Failed installing g++"; fi
if [ $en_jupyter = yes ];  then sudo apt install python3-pip && pip3 install jupyterlab; fi
if [ $en_git = yes ];      then sudo apt install git || echo "Failed installing git"; fi
if [ $en_svn = yes ];      then sudo apt install subversion || echo "Failed installing subversion"; fi
if [ $en_emacs = yes ];    then sudo apt install emacs || echo "Failed installing Emacs"; fi
if [ $en_vim = yes ];      then sudo apt install vim || echo "Failed installing vim"; fi
if [ $en_locate = yes ];   then sudo apt install locate || echo "Failed installing locate"; fi
#=============================================================================================================

# PCB DEVELOPMENT
if [ $en_kicad = yes ];    then sudo apt install kicad || echo "Failed installing kiCAD"; fi
if [ $en_libreCAD = yes ]; then sudo apt install librecad || echo "Failed installing libreCAD"; fi
#=============================================================================================================

# DESKTOP APPLICATIONS
if [ $en_spotify = yes ]; then sudo apt install snap && snap install spotify || echo "Failed installing spotify"; fi
if [ $en_discord = yes];  then sudo snap install discord || echo "Failed installing discord"; fi
#=============================================================================================================

# TERMINAL APPLICATIONS
if [ $en_mutt = yes ]; then sudo apt install mutt || echo "Failed installing mutt"; fi
if [ $en_alcritty = yes ]; then echo "Must fill this alacritty"; fi
#=============================================================================================================

# WINDOW MANAGERS
if [ $en_awesome = yes ]; then sudo apt install awesome || echo "Failed installing awesome"; fi
#=============================================================================================================

# RICE
if [ $en_neofetch = yes]; then sudo apt install neofetch || echo "Failed installing neofetch"; fi
if [ $en_htop ];          then sudo apt install htop || echo "Failed installing htop"; fi
#=============================================================================================================

# WEB-BROWSERS
if [ $en_lynx = yes ];  then sudo apt install lynx || echo "Failed installing lynx"; fi
if [ $en_qute = yes ];  then sudo apt install qutebrowser || echo "Failed installing qutebrowser"; fi
if [ $en_brave = yes ]; then
    sudo apt install apt-transport-https curl
    curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
    echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
    sudo apt update && sudo apt install brave-browser
fi
#=============================================================================================================

# DRIVERS/COMPATIBILITY
#Razer drivers
if [ $en_razer = yes ]; then
    sudo add-apt-repository ppa:openrazer/stable
    sudo add-apt-repository ppa:openrazer/daily
    sudo apt update && sudo apt install openrazer-meta
    #GUI for Razer drivers
    sudo add-apt-repository ppa:polychromatic/stable
    sudo apt update && sudo apt install polychromatic
    #####IF IT BRICKS AND ISNT WORKING
    #sudo apt purge openrazer-meta polychromatic linux-headers-generic
    #sudo apt install linux-headers-generic
    #sudo apt install openrazer-meta polychromatic
    #sudo reboot
fi
#For Wine
if [ $en_wine = yes]; then
    wget -nc https://dl.winehq.org/wine-builds/winehq.key
    sudo apt-key add winehq.key
    sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'
    sudo apt update && sudo apt install --install-recommends winehq-stable
fi
#=============================================================================================================

# MISC
if [ $en_alert = yes ]; then sudo apt install libnotify-bin || echo "Failed installing libnotify-bin"; fi
#=============================================================================================================

#Make sure all packages are up to date
sudo apt upgrade

