sudo apt-get update
sudo apt-get install python
#!/bin/bash

# Set the environment variables
export FLASK_APP=/HSCR/backend-flask/wsgi.py
export FLASK_ENV=production
# Get venv
sudo apt-get install python3-venv

# get OUR REPO
git clone https://github.com/mcbebu/HSCR.git

# Activate the virtual environment (if you are using one)
# If you're not using a virtual environment, you can skip this step
python3 -m venv "/HSCR/backend-flask/venv"
source "/HSCR/backend-flask/venv/bin/activate"

# Install any required dependencies (if necessary)
# If you have already installed your dependencies, you can skip this step
pip install -r "/HSCR/backend-flask/requirements.txt"

# Start the Flask development server
waitress-serve --listen=127.0.0.1:5000 wsgi:app