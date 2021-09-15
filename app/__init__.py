from flask import Flask
# from flask package import Flask. Make sure to install flask into venv

# This is used to relay imports from this file
app = Flask(__name__)

from app import routes
#  from app folder import route object. 
#  This should be placed below because the local host wont run otherwise. order of things
