#!/bin/bash

# Installation script for both Kali Linux and Termux

# Function to install on Kali Linux
install_kali() {
    echo "Installing on Kali Linux..."
    sudo apt update && sudo apt install <your-package> -y
}

# Function to install on Termux
install_termux() {
    echo "Installing on Termux..."
    pkg update && pkg install <your-package> -y
}

# Check the operating system
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        if [[ "$ID" == "kali" ]]; then
            install_kali
        fi
    fi
elif [[ "$OSTYPE" == "termux" ]]; then
    install_termux
else
    echo "Unsupported system."
fi
