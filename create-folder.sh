#!/bin/bash


if [[ -z $1 ]];
then 
    echo "Usage $0 <machine name (without space)>"
else
    echo "Creating nmap,www,dirbuster folders for: $1"
	mkdir $1
	cd $1
	mkdir nmap
	mkdir www
	mkdir dirbuster
    
fi
