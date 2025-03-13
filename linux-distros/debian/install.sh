bash
#!/bin/sh

# Install Debian in Termux
pkg install wget
wget https://raw.githubusercontent.com/Neo-Oli/termux-debian/master/debian.sh
sh debian.sh
