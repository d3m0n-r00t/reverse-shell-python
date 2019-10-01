#!/bin/bash

# bash colors
bold=$(tput bold)
red=$(tput setaf 1)
yellow=$(tput setaf 3)
nocolor=$(tput sgr0)
bold_red=${bold}${red}
bold_yellow=${bold}${yellow}


#getting user input
echo "${yellow}[1]${nocolor} upload.py"
echo "${yellow}[2]${nocolor} host.py"
read  -p ">> " userinput
		case $userinput in
    		1 ) read  -p "${yellow}[^]${nocolor} Enter the Host ip : " newinput
				python3 upload.py $newinput ;;
				2 ) python3 host.py;;
				*) echo "${bold_yellow}[*]${nocolor}Input error."
				exit;;
