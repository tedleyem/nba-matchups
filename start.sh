#!/usr/bin/bash
# Start up development server locally 
#python3 -m pip install --upgrade pip
pip3 install -r requirements.txt

# Set the FLASK_APP environment variable
export FLASK_APP=run.py

# Set up the DEBUG environment
export FLASK_ENV=development

echo ""
echo "Starting Development Server" && sleep 3
echo ""
flask run --host=0.0.0.0 --port=5000