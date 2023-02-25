#!/bin/bash
# for huawei's ec2-user
cd ~
# Update the package list and upgrade installed packages
sudo apt update && sudo apt upgrade -y

# Install necessary packages
sudo apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools git

sudo yum install -y git

# get OUR REPO
git clone https://github.com/mcbebu/HSCR.git

# Change into the repository directory
cd HSCR/backend-flask

# Install required Python packages
sudo pip3 install -r requirements.txt

# Start the Flask development server
gunicorn --bind 0.0.0.0:5000 wsgi:app