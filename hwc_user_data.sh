#!/bin/bash
cd ~
sudo apt update
sudo apt install python3

# get OUR REPO
git clone https://github.com/mcbebu/HSCR.git

# Install any required dependencies (if necessary)
# If you have already installed your dependencies, you can skip this step
pip install -r "HSCR/backend-flask/requirements.txt"

# Start the Flask development server
gunicorn --bind 0.0.0.0:5000 wsgi:app