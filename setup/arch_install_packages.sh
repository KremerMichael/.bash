if [ -f setup.cfg ]; then
    . ./setup.cfg
else
    echo "No config file present, make sure you are running this inside of Scripts/"
fi

if [ en_alacritty = yes ]; then
    sudo pacman -S alacritty
fi

if [ en_awesome = yes ]; then
    sudo pacman -S awesome
fi
